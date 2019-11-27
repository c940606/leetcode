class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        from collections import defaultdict
        import bisect
        sorted_s = sorted(set(s))
        loc = defaultdict(list)

        self.res = None
        for idx, v in enumerate(s):
            loc[v].append(idx)
        print(sorted_s, loc)

        def helper(sorted_s, pre, tmp):
            # print(sorted_s, pre, tmp)
            if not sorted_s:
                self.res = tmp
                return True
            for i in range(len(sorted_s)):
                # print(sorted_s[i])
                if self.res != None:
                    break
                if pre == "#":
                    helper(sorted_s[:i] + sorted_s[i + 1:], loc[sorted_s[i]][0], tmp + sorted_s[i])

                else:
                    l = bisect.bisect_right(loc[sorted_s[i]], pre)
                    if l < len(loc[sorted_s[i]]):
                        helper(sorted_s[:i] + sorted_s[i + 1:], loc[sorted_s[i]][l], tmp + sorted_s[i])

            return False

        helper(sorted_s, "#", "")
        return self.res

    def removeDuplicateLetters2(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        stack = [""]
        existed = set()
        for a in s:
            # print(stack)
            if a not in existed:
                while stack[-1] > a and c[stack[-1]] > 0:
                    existed.remove(stack.pop())
                stack.append(a)
                existed.add(a)
            c[a] -= 1
        return "".join(stack)

    def removeDuplicateLetters3(self, s: str) -> str:
        for a in sorted(set(s)):
            tmp = s[s.index(a):]
            if len(set(tmp)) == len(set(s)):
                return a + self.removeDuplicateLetters(tmp.replace(a, ""))
        return ""

    def removeDuplicateLetters(self, s: str) -> str:
        res = ""
        while s:
            loc = min(map(s.rindex, s))
            a = min(s[:loc + 1])
            res += a
            s = s[s.index(a):].replace(a, "")
        return res


a = Solution()
# print(a.removeDuplicateLetters("bbcaac"))
# print(a.removeDuplicateLetters("bcabc"))
print(a.removeDuplicateLetters("cbacdcbc"))
# print(a.removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic"))

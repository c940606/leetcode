from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        if not s:
            return 0
        s_num = Counter(s)
        low_k = {key for key in s_num if s_num[key] < k}
        # print(low_k)
        left = 0
        right = 0
        n = len(s)
        res = 0
        while right < n:
            tmp = Counter()
            while right < n and s[right] not in low_k:
                tmp[s[right]] += 1
                right += 1
            print(right, tmp)
            while left < right:
                if min([i for i in tmp.values() if i > 0]) >= k:
                    res = max(res, right - left)
                    break
                tmp[s[left]] -= 1
                left += 1
                print(tmp)
            while right < n and s[right] in low_k:
                right += 1
            left = right
            break

        return res

    def longestSubstring1(self, s: str, k: int) -> int:
        # for c in set(s):
        #     if s.count(c) < k:
        #         return max(self.longestSubstring1(i, k) for i in s.split(c))
        # return len(s)
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring1(i, k) for i in s.split(c))

    def longestSubstring2(self, s: str, k: int) -> int:
        n = len(s)
        def helper(s, k, i):
            left, right = 0, 0
            special = 0
            more_k_num = 0
            lookup = Counter()
            res = 0
            while right < n:
                lookup[s[right]] += 1
                if lookup[s[right]] == 1:
                    special += 1
                if lookup[s[right]] == k:
                    more_k_num += 1
                while special > i:
                    lookup[s[left]] -= 1
                    if lookup[s[left]] == 0:
                        special -= 1
                    if lookup[s[left]] == k - 1:
                        more_k_num -= 1
                    left += 1
                if special == more_k_num:
                    res = max(res, right - left + 1)
                right += 1
            return res

        return max(helper(s, k, i) for i in range(1, 27))


a = Solution()
# print(a.longestSubstring("aaabb", 3))
# print(a.longestSubstring(s="ababbc", k=2))
# print(a.longestSubstring("ababacb", 3))
# print(a.longestSubstring("bbaaacbd", 3))
print(a.longestSubstring2("baaabcb", 3))

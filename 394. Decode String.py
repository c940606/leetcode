class Solution:
    def decodeString1(self, s: str) -> str:
        def matchBracket(s):
            pairBracket = {}
            stack = []
            for idx, val in enumerate(s):
                if val == "[":
                    stack.append(idx)
                if val == "]":
                    pairBracket[stack.pop()] = idx
            return pairBracket

        # print(pairBracket)

        def helper(s, pairBracket):
            if "[" not in s:
                return s
            left_p = s.find("[")
            right_p = pairBracket[left_p]
            i = 0
            while not s[i].isdigit():
                i += 1
            return s[:i] + int(s[i:left_p]) * helper(s[left_p + 1: right_p], matchBracket(s[left_p + 1: right_p])) + \
                   helper(s[right_p + 1:], matchBracket(s[right_p + 1:]))

        return helper(s, matchBracket(s))

    def decodeString2(self, s: str) -> str:
        pos = 0

        def helper():
            nonlocal pos
            num = 0
            word = ""
            while pos < len(s):
                cur = s[pos]
                if cur == '[':
                    pos += 1
                    curStr = helper()
                    word += num * curStr
                    num = 0
                elif cur.isdigit():
                    num = num * 10 + int(cur)
                elif cur == ']':
                    return word
                else:
                    word += cur
                pos += 1
            return word

        return helper()

    def decodeString(self, s: str) -> str:
        stack = []
        curStr = ""
        curNum = 0
        for a in s:
            if a == '[':
                stack.append(curNum)
                stack.append(curStr)
                curStr = ""
                curNum = 0
            elif a.isdigit():
                curNum = curNum * 10 + int(a)
            elif a == ']':
                curStr = stack.pop() + stack.pop() * curStr
            else:
                curStr += a
        return curStr


a = Solution()
print(a.decodeString("3[a]2[bc]"))
print(a.decodeString("3[a2[c]]"))
print(a.decodeString("2[abc]3[cd]ef"))

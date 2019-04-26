class Solution:
    def removeOuterParentheses(self, S):
        if not S:
            return ""
        stack = [S[0]]
        left = 0
        res = ""
        for idx, s in enumerate(S[1:], 1):
            if s == "(":
                stack.append(s)
            elif s == ")":
                stack.pop()
            if not stack:
                res += S[left + 1:idx]
                left = idx + 1
        return res

    def removeOuterParentheses1(self, S):
        opened = 0
        res = []
        for c in S:
            if c == "(" and opened > 0:
                res.append(c)
            if c == ")" and opened > 1:
                res.append(c)
            opened += 1 if c == "(" else -1
        return "".join(res)


a = Solution()
print(a.removeOuterParentheses("(()())(())"))
print(a.removeOuterParentheses(""))
print(a.removeOuterParentheses("(()())(())(()(()))"))
print(a.removeOuterParentheses("()()"))

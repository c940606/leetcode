class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ""
        for a in s:
            if a == ")":
                loc = stack.rfind("(")
                stack = stack[:loc] + stack[loc + 1: ][::-1]
            else:
                stack += a
        return stack

a = Solution()
print(a.reverseParentheses("(abcd)"))
print(a.reverseParentheses(s = "(u(love)i)"))
print(a.reverseParentheses(s = "(ed(et(oc))el)"))
print(a.reverseParentheses(s = "a(bcdefghijkl(mno)p)q"))
print(a.reverseParentheses("a"))

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = 0
        res = ""
        for a in s:
            if a == "(":
                l += 1
                res += a
            elif a == ")":
                if l <= 0:
                    continue
                l -= 1
                res += a
            else:
                res += a
        # print(res)
        return res[::-1].replace("(", "", l)[::-1]


a = Solution()
print(a.minRemoveToMakeValid("())()((("))
print(a.minRemoveToMakeValid("lee(t(c)o)de)"))
print(a.minRemoveToMakeValid(s = "))(("))
print(a.minRemoveToMakeValid(s = "(a(b(c)d)"))
print(a.minRemoveToMakeValid(s = "a)b(c)d"))

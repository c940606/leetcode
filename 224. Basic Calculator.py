class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        i = 0
        n = len(s)
        res = 0
        stack = []
        while i < n :
            if s[i].isdigit():
                tmp = s[i]
                while i < n - 1 and s[i+1].isdigit():
                    i += 1
                    tmp += s[i]
                res += int(tmp) * sign
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ")":
                res = res*stack.pop() + stack.pop()
            i += 1
        return res


a = Solution()
print(a.calculate("1+1"))
print(a.calculate("2-1+2"))
print(a.calculate("(1+(4+5+2)-3)+(6+8)"))

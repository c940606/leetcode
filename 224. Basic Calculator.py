class Solution:
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        i = 0
        n = len(s)
        res = 0
        stack = []
        while i < n:
            if s[i].isdigit():
                tmp = s[i]
                while i < n - 1 and s[i + 1].isdigit():
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
                res = res * stack.pop() + stack.pop()
            i += 1
        return res

    def calculate2(self, s):
        res = 0
        stack = []
        sign = 1
        i = 0
        n = len(s)
        while i < n:

            if s[i] == " ":
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                i += 1
            elif s[i] == ")":
                # print(stack)
                res = res * stack.pop() + stack.pop()
                i += 1
            elif s[i].isdigit():
                tmp = int(s[i])
                i += 1
                while i < n and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                res += tmp * sign
        return res

    def calculate(self, s):
        stack = []
        # 记录数字的符号, 因为题目说没有负数,说明第一个为正数,设为1
        sign = 1
        # 数字
        num = 0
        # 结果
        res = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                # 为下一次做准备
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                # 为下一次做准备
                num = 0
                sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ")":
                res += sign * num
                num = 0
                res = stack.pop() * res + stack.pop()
        res += sign * num
        return res


a = Solution()
print(a.calculate("2147483647"))
print(a.calculate("(1 + 1)"))
print(a.calculate("2-1+2"))
print(a.calculate("(1+(4+5+2)-3)+(6+8)"))
print(a.calculate("(1-(3-4))"))
print(a.calculate("(7)-(0)+(4)"))
print(a.calculate("7 - 0 + 4"))

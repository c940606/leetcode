class Solution:
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        operation = {
            "+",
            "-",
            "*",
            "/",
        }
        expression = []
        n = len(s)
        start = 0
        while start < n:
            end = start
            while end < n and s[end] not in operation:
                end += 1
            # print(start,end)
            expression.append(int("".join(s[start:end].split())))
            if end < n and s[end] in operation:
                expression.append(s[end])
            start = end + 1
        print(expression)
        expression_n = len(expression)
        if expression_n == 1:
            return expression[0]
        tmp = []
        for i in range(1, expression_n, 2):
            if expression[i] == "*":
                tmp.append(expression[i - 1] * expression[i + 1])
            elif expression[i] == "/":
                tmp.append(expression[i - 1] // expression[i + 1])
            else:
                tmp.append(expression[i - 1])
                tmp.append(expression[i])
        print(tmp)
        if tmp[-1] == "+" or tmp[-1] == "-":
            tmp.append(expression[-1])
        res = tmp[0]
        print(tmp)
        expression_n1 = len(tmp)
        # print(expression_n1)
        j = 1
        while j < expression_n1:
            if tmp[j] == "+":
                res += tmp[j + 1]
            elif tmp[j] == "-":
                res -= tmp[j + 1]
            j += 2
        return res

    def calculate2(self, s):
        s = s.strip()
        stack = []
        i = 0
        while i < len(s):
            # print(i)
            if s[i].isdigit():
                tmp = ""
                while i < len(s) and s[i].isdigit():
                    tmp += s[i]
                    i += 1
                stack.append(int(tmp))
            elif s[i] in "+-":
                stack.append(s[i])
                i += 1
            elif s[i] in "*/":
                op = s[i]
                i += 1
                while i < len(s) and s[i] == " ":
                    i += 1
                tmp = ""
                while i < len(s) and s[i].isdigit():
                    tmp += s[i]
                    i += 1
                if op == "*":
                    stack.append(stack.pop() * int(tmp))
                if op == "/":
                    stack.append(stack.pop() // int(tmp))
            else:
                i += 1
        res = 0
        op = 1
        for t in stack:
            if t == "+":
                op = 1
            elif t == "-":
                op = -1
            else:
                res += op * t
        return res

    def calculate(self, s):
        s += "+0"
        stack = []
        num = 0
        # 记录前一个符号
        sign = "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in {"+", "-", "*", "/"}:
                # print(sign, num)
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                sign, num = c, 0
        return sum(stack)


a = Solution()
print(a.calculate("3+2*2"))
print(a.calculate(" 3/2 "))
print(a.calculate(" 3+5 / 2 "))
print(a.calculate("0"))
print(a.calculate("1 + 1"))
print(a.calculate("3+2*2"))
print(a.calculate("2*3+4"))

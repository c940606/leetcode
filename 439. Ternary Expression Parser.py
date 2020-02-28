class Solution:
    def parseTernary1(self, expression: str) -> str:
        stack = []
        for exp in reversed(expression):

            if stack and stack[-1] == "?":
                # 弹出问号
                stack.pop()
                val1 = stack.pop()
                # 弹出:
                stack.pop()
                val2 = stack.pop()
                if exp == "T":
                    stack.append(val1)
                else:
                    stack.append(val2)
            else:
                stack.append(exp)
        return stack.pop()

    def parseTernary(self, expression: str) -> str:
        if len(expression) == 1:
            return expression[0]
        num = 1
        pos = 2
        while pos < len(expression) and num > 0:
            if expression[pos] == "?":
                num += 1
            elif expression[pos] == ":":
                num -= 1
            pos += 1
        #print(pos)
        #print(pos,expression[pos] ,expression[2:pos-1], expression[pos+1:])
        if expression[0] == "T":
            return self.parseTernary(expression[2:pos - 1])
        else:
            return self.parseTernary(expression[pos:])


a = Solution()
print(a.parseTernary("T?F?F:5:3"))
print(a.parseTernary("T?T?F:5:3"))
print(a.parseTernary("F?1:T?4:5"))
print(a.parseTernary("T?T:F?T?1:2:F?3:4"))
# print(a.parseTernary("T?T?5:F?7:7"))
print(a.parseTernary(
    "F?T?2:6:T?T?5:F?7:7:T?6:T?2:F?T:T?2:T?T?F?F?F?4:T?F?5:T?F:T?F?4:9:9:6:3:9:5:T?F?F?F?F?5:2:9:6:F?4:T?6:7:T?8:F?0:F?F?5:T?F:5:T?T?9:4:F?F?T?F?F?6:8:F:4:F?F?T?F:F?F?0:F?7:2:T?8:T?F?9:8:7:1:6:T?T?F?9:T?F?3:8:3:F:4"))  # 5

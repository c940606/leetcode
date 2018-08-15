import math
class Solution(object):
	def evalRPN(self, tokens):
		"""
		根据逆波兰表示法，求表达式的值。
		有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
		----
		输入: ["2", "1", "+", "3", "*"]
		输出: 9
		解释: ((2 + 1) * 3) = 9
		---
		思路：
		用栈
		1.遇到数字放进栈中
		2. 遇到运算符 就把栈中弹出来 结果再压入栈中
		3. 最后弹出栈中结果
		:type tokens: List[str]
		:rtype: int
		"""
		operators = ["+","-","*","/"]
		stack = []
		for i in range(len(tokens)):
			if tokens[i] not in operators:
				stack.append(tokens[i])
			else:
				num1 = int(stack.pop())
				num2 = int(stack.pop())
				o_index = operators.index(tokens[i])
				if o_index == 0:
					res = num2+num1
				elif o_index == 1:
					res = num2-num1
				elif o_index == 2:
					res = num2 * num1
				elif o_index == 3:
					res = int(math.modf(num2/num1)[1])
				print(res)
				stack.append(res)
		return  stack.pop()
a = Solution()
print(a.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
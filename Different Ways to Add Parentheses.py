class Solution(object):
	def __init__(self):
		self.lookup = {}
	def diffWaysToCompute(self, input):
		"""
		给定一个含有数字和运算符的字符串，为表达式添加括号，
		改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
		---
		输入: "2-1-1"
		输出: [0, 2]
		解释:
		((2-1)-1) = 0
		(2-(1-1)) = 2
		--
		输入: "2*3-4*5"
		输出: [-34, -14, -10, -10, 10]
		解释:
		(2*(3-(4*5))) = -34
		((2*3)-(4*5)) = -14
		((2*(3-4))*5) = -10
		(2*((3-4)*5)) = -10
		(((2*3)-4)*5) = 10
		---

		:type input: str
		:rtype: List[int]
		"""
		if input.isdigit():
			return [int(input)]
		if input in self.lookup:
			return self.lookup[input]
		res = []
		for i in range(len(input)):
			if input[i] in "-+*":
				res1 = self.diffWaysToCompute(input[:i])

				res2 = self.diffWaysToCompute(input[i+1:])

				for j in res1:
					for k in res2:
						print(j,k,input[i])
						res.append(self.helper(j,k,input[i]))
				print("res:",res)
		# print(res)
		self.lookup[input] = res
		return res
	def helper(self,m,n,op):
		if op == "+":
			return m+n
		elif op == "-":
			return m-n
		else:
			return m*n
a = Solution()
print(a.diffWaysToCompute("2-1-1"))

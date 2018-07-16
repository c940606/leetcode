class Solution:
	def generateParenthesis(self, n):
		"""
		给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合
		---------------
		例如，给出 n = 3，生成结果为：
			[
			  "((()))",
			  "(()())",
			  "(())()",
			  "()(())",
			  "()()()"
			]
		:type n: int
		:rtype: List[str]
		"""
		self.res = []
		self.singStr("",0,0,n)
		return  self.res
	def singStr(self,s,left_parenthesis,righ_parenthesis,n):
		if left_parenthesis == n and righ_parenthesis == n :
			print(s)
			self.res.append(s)
		if left_parenthesis < n:
			self.singStr(s+"(",left_parenthesis+1,righ_parenthesis,n)
		if left_parenthesis > righ_parenthesis:
			self.singStr(s+")",left_parenthesis,righ_parenthesis+1,n)
a = Solution()
print(a.generateParenthesis(13))
print(len(a.res))
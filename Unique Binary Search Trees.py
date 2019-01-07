class Solution:
	def numTrees(self, n):
		"""
		给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
		---
		输入: 3
		输出: 5
		:type n: int
		:rtype: int
		"""
		self.lookup = [1 for _ in range(n+1)]
		# print(self.lookup)
		if n >1 :
			for i in range(2,n+1):
				self.lookup[i] = self.help(i)
				# print(self.lookup)
		return self.lookup[-1]

	def help(self, i):
		sum = 0
		for j in range(0,i):#i = 3
			sum += self.lookup[j]*self.lookup[i-j-1]

			# print("---",sum)
		return sum

	def numTrees1(self, n):

a = Solution()
print(a.numTrees(5))




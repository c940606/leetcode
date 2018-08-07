class Solution:
	def grayCode(self, n):
		"""
		格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
		给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
		:type n: int
		:rtype: List[int]
		"""
		if n == 0:
			return [0]
		self.nums = ["0","1"]
		self.res = []
		self.trace("",n)
		return self.res
	def trace(self,s,n):
		if n == 0:
			self.res.append(int(s,2))
		else:
			for item in self.nums:
				self.trace(s+item,n-1)
a = Solution()
print(a.grayCode(2))



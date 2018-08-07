class Solution:
	def generate(self, numRows):
		"""
		给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
		:type numRows: int
		:rtype: List[List[int]]
		"""
		res = [[1]*i for i in range(1,numRows+1)]
		if numRows <=2:
			return res
		for i in range(2,numRows):
			for j in range(1,i):
				res[i][j] = res[i-1][j]+res[i-1][j-1]
		return res
	
a = Solution()
print(a.generate(33))


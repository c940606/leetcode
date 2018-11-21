class Solution(object):
	def matrixScore(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		if not A:
			return 0
		row = len(A)
		col = len(A[0])
		print("初始值：",A)
		for i in range(row):
			if A[i][0] == 0:
				for j in range(col):
					A[i][j] = 1 - A[i][j]
		print("首列全为0:",A)
		base = 1
		res = 0
		for k in range(col-1,-1,-1):
			temp_one = sum([A[i][k] for i in range(row)])
			max_col_one = max(temp_one,row - temp_one)
			temp = max_col_one*base
			res += temp
			base = base << 1
		return res
a = Solution()
print(a.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
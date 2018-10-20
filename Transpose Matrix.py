class Solution(object):
	def transpose(self, A):
		"""
		:type A: List[List[int]]
		:rtype: List[List[int]]
		"""
		row = len(A)
		col = len(A[0])
		res = [[0]*row for _ in range(col)]
		for i in range(row):
			for j in range(col):
				res[i][j] = A[j][i]
		return res

	def transpose1(self, A):
		return list(map(list,zip(*A)))
a = Solution()
print(a.transpose1([[1,2,3],[4,5,6],[7,8,9]]))
import copy
class Solution:
	def setZeroes(self, matrix):
		"""
		给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		m = len(matrix)
		n = len(matrix[0])

		def setZer0(i,j):
			for k in range(n):
				matrix[i][k] = 0
			for k in range(m):
				matrix[k][j] = 0
		new_matrix = copy.deepcopy(matrix)
		for i in range(m):
			for j in range(n):
				if new_matrix[i][j] == 0:
					setZer0(i,j)
		return matrix
a =  Solution()
obj = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
print(a.setZeroes(obj))
class Solution(object):
	def isToeplitzMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: bool
		"""
		if not matrix:
			return False
		row = len(matrix)
		col = len(matrix[0])

		for j in range(col):
			i = 0
			temp_num = matrix[i][j]
			temp_j = j
			while i < row and temp_j < col:
				if temp_num == matrix[i][temp_j]:
					i += 1
					temp_j += 1
				else:
					return False
		for i in range(1,row):
			temp_i = i
			j = 0
			temp_num = matrix[i][j]
			while temp_i < row and j < col:
				if temp_num == matrix[temp_i][j]:
					temp_i += 1
					j += 1
				else:
					return False
		return True
a = Solution()
print(a.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(a.isToeplitzMatrix([[1,2],[2,2]]))




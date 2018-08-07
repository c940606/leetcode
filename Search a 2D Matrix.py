class Solution:
	def searchMatrix(self, matrix, target):
		"""
		编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
			每行中的整数从左到右按升序排列。
			每行的第一个整数大于前一行的最后一个整数。
		---
		输入:
			matrix = [
			  [1,   3,  5,  7],
			  [10, 11, 16, 20],
			  [23, 30, 34, 50]
			]
			target = 3
			输出: true
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		m = len(matrix)
		# n = len(matrix[0])
		i = 0
		j = m-1
		while i < j:#[[1],[3],[5]]
			mid = (i+j)//2
			if target >= matrix[j][0]:
				return target in matrix[j]
			elif target == matrix[mid][0]:
				return True
			elif target > matrix[mid][0]:
				i = mid
				if j -i == 1:
					return target in matrix[i]
			elif target < matrix[mid][0]:
				j = mid
				if j -i == 1:
					return target in matrix[i]
		return target in matrix[0]



matrix = [
			  [1,   3,  5,  7],
			  [10, 11, 16, 20],
			  [23, 30, 34, 50]
			]
matrix2 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
matrix3 = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

a = Solution()
print(a.searchMatrix(matrix3,55))
class Solution(object):
	def __init__(self):
		self.lookup = {}

	def longestIncreasingPath(self, matrix):
		"""
		给定一个整数矩阵，找出最长递增路径的长度。
		对于每个单元格，你可以往上，下，左，右四个方向移动。
		你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
		---
		输入: nums =
		[
		  [9,9,4],
		  [6,6,8],
		  [2,1,1]
		]
		输出: 4
		解释: 最长递增路径为 [1, 2, 6, 9]。
		---
		深度遍历
		要记录
		:type matrix: List[List[int]]
		:rtype: int
		"""
		row = len(matrix)
		col = len(matrix[0])
		dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
		res = 1
		def dfs(matrix,i,j,row,col):
			if (i,j) in self.lookup:
				return self.lookup[(i,j)]
			ij_max_len = 1
			for dir in dirs:
				x = i + dir[0]
				y = j + dir[1]
				if x < 0 or x >= row or y < 0 or y >= col or matrix[x][y] <= matrix[i][j]:
					continue
				temp_len = 1 + dfs(matrix,x,y,row,col)
				print(i,j)

				ij_max_len = max(ij_max_len,temp_len)
			self.lookup[(i,j)] = ij_max_len
			print(self.lookup)

			return ij_max_len
		for i in range(row):
			for j in range(col):
				temp = dfs(matrix,i,j,row,col)
				res = max(res,temp)
		# print("------")
		# print(self.lookup)
		return res


a = Solution()
print(a.longestIncreasingPath([
	[9, 9, 4],
	[6, 6, 8],
	[2, 1, 1]
]))

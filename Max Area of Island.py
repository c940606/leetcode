import copy


class Solution(object):
	def maxAreaOfIsland(self, grid):
		"""
		给定一个包含了一些 0 和 1的非空二维数组 grid ,
		一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
		找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
		---
		[[0,0,1,0,0,0,0,1,0,0,0,0,0],
		 [0,0,0,0,0,0,0,1,1,1,0,0,0],
		 [0,1,1,0,1,0,0,0,0,0,0,0,0],
		 [0,1,0,0,1,1,0,0,1,0,1,0,0],
		 [0,1,0,0,1,1,0,0,1,1,1,0,0],
		 [0,0,0,0,0,0,0,0,0,0,1,0,0],
		 [0,0,0,0,0,0,0,1,1,1,0,0,0],
		 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
		 最大值6
		 ---

		:type grid: List[List[int]]
		:rtype: int
		"""
		row = len(grid)
		col = len(grid[0])
		board = [[0]*col for _ in range(row)]
		def helper(i,j):
			board[i][j]  = 1
			# 上
			count = 1
			if i>0 and grid[i-1][j] == 1 and board[i-1][j] == 0:
				count += helper(i-1,j)
			# xia
			if i < row-1 and grid[i+1][j]== 1 and board[i+1][j]==0:
				count += helper(i+1,j)
			# zuo
			if j>0 and grid[i][j-1] == 1 and board[i][j-1]==0:
				count += helper(i,j-1)
			if j<col-1 and grid[i][j+1] == 1 and board[i][j+1]==0:
				count += helper(i,j+1)
			return count
		res = 0
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1 and board[i][j] == 0:
					temp = helper(i,j)
					res = max(res,temp)
		return  res
a = Solution()
print(a.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
		 [0,0,0,0,0,0,0,1,1,1,0,0,0],
		 [0,1,1,0,1,0,0,0,0,0,0,0,0],
		 [0,1,0,0,1,1,0,0,1,0,1,0,0],
		 [0,1,0,0,1,1,0,0,1,1,1,0,0],
		 [0,0,0,0,0,0,0,0,0,0,1,0,0],
		 [0,0,0,0,0,0,0,1,1,1,0,0,0],
		 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
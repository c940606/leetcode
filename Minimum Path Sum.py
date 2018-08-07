class Solution:
	def minPathSum(self, grid):
		"""
		给定一个包含非负整数的 m x n 网格，
		请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
		:type grid: List[List[int]]
		:rtype: int
		"""
		m = len(grid)
		n = len(grid[0])
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					continue
				elif i ==0:
					grid[i][j] += grid[i][j-1]
				elif j == 0:
					grid[i][j] += grid[i-1][j]
				else:
					grid[i][j] += min(grid[i-1][j],grid[i][j-1])
		return grid[m-1][n-1]
a = Solution()
obj = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(a.minPathSum(obj))


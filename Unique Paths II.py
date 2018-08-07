class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
		机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
		现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
		---
		输入:
			[
			  [0,0,0],
			  [0,1,0],
			  [0,0,0]
			]
			输出: 2
			解释:
			3x3 网格的正中间有一个障碍物。
			从左上角到右下角一共有 2 条不同的路径：
			1. 向右 -> 向右 -> 向下 -> 向下
			2. 向下 -> 向下 -> 向右 -> 向右
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		if m == 1 or n == 1:
			return 1
		trace = [[0]*n for _ in range(m)]
		print(trace)

		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
					trace[0][0] = 1
				elif i == 0 and j>0:
					if obstacleGrid[i][j] == 1:
						trace[i][j] = 0
					else:
						trace[i][j] = trace[i][j-1]
				elif j == 0 and i>0:
					if obstacleGrid[i][j] == 1:
						trace[i][j] = 0
					else:
						trace[i][j] = trace[i-1][j]
				elif obstacleGrid[i][j] == 1:
					trace[i][j] = 0

				else:
					trace[i][j] = trace[i][j-1] + trace[i-1][j]
		return trace[m-1][n-1]
a = Solution()
obj1 = [
			  [0,0,0],
			  [0,1,0],
			  [0,0,0]
			]
obj2 = [[0,0],[1,1],[0,0]]
obj = [[1]]
print(a.uniquePathsWithObstacles(obj2))



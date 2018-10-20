class Solution(object):
	def projectionArea(self, grid):
		"""
		在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。
		每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
		现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
		投影就像影子，将三维形体映射到一个二维平面上。
		在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。
		返回所有三个投影的总面积。
		---
		思路:
		俯视图:
			每个坐标数>0 就算一个面积
		左视图:
			求行最大的
		右视图:
			求列最大的
		:type grid: List[List[int]]
		:rtype: int
		"""
		row = len(grid)
		col = len(grid[0])
		# 俯视图
		down_area = 0
		for i in range(row):
			for j in range(col):
				if grid[i][j] != 0:
					down_area += 1
		# 左视图
		left_area = 0
		for i in range(row):
			left_area += max(grid[i])
		# 右视图
		right_area = 0
		# for i in range(col):
		# 	temp_max = 0
		# 	for j in range(row):
		# 		if temp_max < grid[j][i]:
		# 			temp_max = grid[j][i]
		# 	right_area += temp_max
		for i in zip(*grid):
			print(i)
			right_area += max(i)
		return down_area + left_area + right_area
a = Solution()
print(a.projectionArea([[2]]))
print(a.projectionArea([[1,2],[3,4]]))
print(a.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))
print(a.projectionArea([[2,2,2],[2,1,2],[2,2,2]]))

class Solution(object):
	def islandPerimeter(self, grid):
		"""
		给定一个包含 0 和 1 的二维网格地图，
		其中 1 表示陆地 0 表示水域。
		网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，
		但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
		岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
		格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
		:type grid: List[List[int]]
		:rtype: int
		"""
		row = len(grid)
		col = len(grid[0])
		flag = []
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1:
					flag.append((i,j))
		def helper(item):
			count = 4
			if (item[0]-1,item[1]) in flag:
				count -= 1
			if (item[0] + 1, item[1]) in flag:
				count -= 1
			if (item[0] , item[1]-1) in flag:
				count -= 1
			if (item[0] , item[1]+1) in flag:
				count -= 1
			return count
		binchang = 0
		for item in flag:
			temp = helper(item)
			binchang += temp
		return binchang

	def islandPerimeter1(self, grid):
		row = len(grid)
		col = len(grid[0])
		binchang = 0
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1:
					count = 4
					if i > 0 and grid[i-1][j] == 1:
						count -= 1
					if i < row-1 and grid[i+1][j] == 1:
						count -= 1
					if j > 0 and grid[i][j-1] == 1:
						count -= 1
					if j < col -1 and grid[i][j+1] == 1:
						count -= 1
					binchang += count
		return binchang
a = Solution()
print(a.islandPerimeter1([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))

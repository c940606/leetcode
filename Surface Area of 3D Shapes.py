class Solution(object):
	def surfaceArea(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		upper_area = 0
		m = len(grid)
		n = len(grid[0])
		for i in range(m):
			for j in range(n):
				if grid[i][j] != 0:
					upper_area += 1
		front_area = 0
		for i in grid:
			front_area += max(i)
		left_area = 0
		for j in zip(*grid):
			left_area += max(j)
		nubu_area = 0
		for i in range(1,m-1):
			for j in range(1,n-1):
				if grid[i-1][j] > grid[i][j]:
					nubu_area += (grid[i-1][j]-grid[i][j])
				if grid[i + 1][j] > grid[i][j]:
					nubu_area += (grid[i +1][j] - grid[i][j])
				if grid[i][j-1] > grid[i][j]:
					nubu_area += (grid[i][j-1]-grid[i][j])
				if grid[i][j+1] > grid[i][j]:
					nubu_area += (grid[i][j+1]-grid[i][j])
		waiceng = 0
		
		return 2*(upper_area+front_area+left_area)+nubu_area
a = Solution()
# print(a.surfaceArea([[2]]))
# print(a.surfaceArea([[1,2],[3,4]]))
# print(a.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
# print(a.surfaceArea([[1,0],[0,2]]))
# print(a.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
print(a.surfaceArea([[3,3,3],[3,4,5],[5,0,4]]))
class Solution(object):
	def maxIncreaseKeepingSkyline(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		col_max = []
		row_max = []
		for item in zip(*grid):
			col_max.append(max(item))
		for item in grid:
			row_max.append(max(item))
		res = []
		print(col_max)
		print(row_max)
		for i in row_max:
			temp = []
			for j in col_max:
				temp.append(min(i,j))
			res.append(temp)
		return sum(map(sum,res))-sum(map(sum,grid))
a = Solution()
print(a.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
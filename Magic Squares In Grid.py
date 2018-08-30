class Solution(object):
	def numMagicSquaresInside(self, grid):
		"""
		3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
		给定一个由整数组成的 N × N 矩阵，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
		---
		输入: [[4,3,8,4],
			  [9,5,1,9],
			  [2,7,6,2]]
		输出: 1
		解释:
		下面的子矩阵是一个 3 x 3 的幻方：
		438
		951
		276

		而这一个不是：
		384
		519
		762
		---
		思路：
		先找出所有3x3的矩阵，然后验证他们是不是行列对象是否相等
		:type grid: List[List[int]]
		:rtype: int
		"""
		count = 0
		jup_max = []
		row = len(grid)
		col = len(grid[0])
		for i in range(0,row-2):
			for j in range(0,col-2):
				temp = []
				temp.append(grid[i][j:j+3])
				temp.append(grid[i+1][j:j+3])
				temp.append(grid[i+2][j:j+3])
				jup_max.append(temp)
		for item in jup_max:
			if self.jup(item):
				count+= 1
		return count


		return jup_max
	def jup(self,matr):
		print(matr)
		temp = matr[0]+matr[1]+matr[2]
		if max(temp)>9 or min(temp)< 1 or len(set(temp)) != 9:
			return False

		if sum(matr[0]) == sum(matr[1]) == sum(matr[2]) == sum([matr[0][0],matr[1][0],matr[2][0]]) == sum([matr[0][1],matr[1][1],matr[2][1]]) == sum([matr[0][2],matr[1][2],matr[2][2]]) == sum([matr[0][0],matr[1][1],matr[2][2]])==sum([matr[0][2],matr[1][1],matr[2][0]]):
			return True
		else:
			return False
a = Solution()
print(a.numMagicSquaresInside([[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]))

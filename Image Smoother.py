class Solution(object):
	def imageSmoother(self, M):
		"""
		包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，
		平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
		--
		输入:
		[[1,1,1],
		 [1,0,1],
		 [1,1,1]]
		输出:
		[[0, 0, 0],
		 [0, 0, 0],
		 [0, 0, 0]]
		解释:
		对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
		对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
		对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
		---
		注意:
		给定矩阵中的整数范围为 [0, 255]。
		矩阵的长和宽的范围均为 [1, 150]。
		---
		思路 遍历周围8个
		:type M: List[List[int]]
		:rtype: List[List[int]]
		"""
		n = len(M)
		m = len(M[0])
		res = [[0]*m for _ in range(n)]
		def helper(i,j):
			all_sum = 0
			col_sum = 0
			if i-1>=0 and j-1>=0:
				all_sum += 1
				col_sum += M[i-1][j-1]
			if j-1>=0:
				all_sum += 1
				col_sum += M[i][j-1]
			if i+1< n and j-1>=0:
				all_sum += 1
				col_sum += M[i+1][j-1]
			if i-1 >= 0:
				all_sum += 1
				col_sum += M[i-1][j]
			if i+1< n :
				all_sum += 1
				col_sum += M[i+1][j]
			if i-1 >= 0 and j+1 < m:
				all_sum += 1
				col_sum += M[i-1][j+1]
			if j+1 < m:
				all_sum += 1
				col_sum += M[i][j+1]
			if i +1 <n and j+1 < m:
				all_sum += 1
				col_sum += M[i+1][j+1]
			all_sum += 1
			col_sum += M[i][j]
			return int(col_sum/all_sum)
		for i in range(n):
			for j in range(m):
				res[i][j] = helper(i,j)
		return res
a = Solution()
print(a.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))


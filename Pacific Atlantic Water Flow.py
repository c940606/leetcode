class Solution:
	def pacificAtlantic(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		if not matrix: return []
		step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		res = []
		row = len(matrix)
		col = len(matrix[0])
		q_flag = [[False] * col for _ in range(row)]
		a_flag = [[False] * col for _ in range(row)]

		def dfs(i, j, visited):
			visited[i][j] = True
			for x, y in step:
				tmp_i, tmp_j = i + x, j + y
				if tmp_i < 0 or tmp_j < 0 or tmp_i >= row or tmp_j >= col or matrix[tmp_i][tmp_j] < matrix[i][
					j] or visited[tmp_i][tmp_j]:
					continue
				dfs(tmp_i, tmp_j, visited)

		for m in range(row):
			dfs(m, 0, q_flag)
			dfs(m, col - 1, a_flag)
		for n in range(col):
			dfs(0, n, q_flag)
			dfs(row - 1, n, a_flag)
		for i in range(row):
			for j in range(col):
				if q_flag[i][j] and a_flag[i][j]:
					res.append([i, j])
		return res


a = Solution()
print(a.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

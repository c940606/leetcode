class Solution:
	def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
		queue = []
		row, col = len(matrix), len(matrix[0])
		for i in range(row):
			for j in range(col):
				if matrix[i][j] == 0:
					queue.append([i, j])
				else:
					matrix[i][j] = float("inf")
		step = 1
		while queue:
			nxt_queue = []
			for i, j in queue:
				for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
					tmp_i, tmp_j = i + x, j + y
					if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[tmp_i][tmp_j] > step:
						matrix[tmp_i][tmp_j] = step
						nxt_queue.append([tmp_i, tmp_j])
			step += 1
			queue = nxt_queue
		return matrix

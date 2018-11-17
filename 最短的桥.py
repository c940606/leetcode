class Solution(object):
	def shortestBridge(self, A):
		"""
		在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
		现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
		返回必须翻转的 0 的最小数目。（可以保证答案至少是 1。）
		---
		输入：[[0,1],[1,0]]
		输出：1
		--
		输入：[[0,1,0],[0,0,0],[0,0,1]]
		输出：2
		---
		输入：[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
		输出：1
		--
		思路:
		1. 先找第一个岛
		2. bfs
		:type A: List[List[int]]
		:rtype: int
		"""
		row = len(A)
		col = len(A[0])
		# ranse dfs
		visited = set()
		def helper1(i,j):
			A[i][j] = 2
			visited.add((i,j))
			if i>0 and (i-1,j) not in visited and A[i-1][j]==1:
				helper1(i-1,j)
				visited.add((i-1,j))
			if i<row-1 and (i+1,j) not in visited and A[i+1][j]== 1:
				helper1(i+1,j)
				visited.add((i+1,j))
			if j>0 and (i,j-1) not in visited and A[i][j-1]==1:
				helper1(i,j-1)
				visited.add((i,j-1))
			if j<col-1 and (i,j+1) not in visited and A[i][j+1] == 1:
				helper1(i,j+1)
				visited.add((i,j+1))
		# bfs
		def helper2(i,j):
			queue = [(i,j)]
			run = {(i,j)}
			while queue:
				i,j = queue.pop(0)
				A[i][j] = 2
				if i>0 and (i-1,j) not in run and A[i-1][j] == 1:
					queue.append((i-1,j))
					run.add((i-1,j))
				if i < row-1 and (i+1,j) not in run  and A[i+1][j] == 1:
					queue.append((i+1,j))
					run.add((i+1,j))
				if j > 0 and (i,j-1) not in run and A[i][j-1] == 1:
					queue.append((i,j-1))
					run.add((i,j-1))
				if j < col-1 and (i,j+1) not in run and A[i][j+1] == 1:
					queue.append((i,j+1))
					run.add((i,j+1))
		flag = False
		for i in range(row):
			if flag:
				break
			for j in range(col):
				if A[i][j] == 1:
					helper2(i,j)
					flag = True
					break
		print(A)
		queue = []
		visited1 = set()
		# visited2 = set()
		# min_step = 101
		# def helper3(i,j,step):
		# 	visited2.add((i,j))

		for i in range(row):
			for j in range(col):
				if A[i][j] == 1:
					# bfs
					queue.append((i,j,0))
					visited1.add((i,j))
		# 			# dfs
		# 			helper3(i,j,0)
		# print(min_step)
					# bfs
		# while queue:
			i,j,step = queue.pop(0)
			if (i>0 and A[i-1][j] == 2) or (i<row-1 and A[i+1][j] == 2) \
					or ( j > 0 and A[i][j-1] == 2) or (j<col-1 and A[i][j+1]==2):
				return step
			if i > 0 and (i-1,j) not in visited1 and A[i-1][j] == 0:
				queue.append((i-1,j,step+1))
				visited1.add((i-1,j))
			if i < row -1 and (i+1,j) not in visited1 and A[i+1][j] == 0:
				queue.append((i+1,j,step+1))
				visited1.add((i+1,j))
			if j > 0 and (i,j-1) not in visited1 and A[i][j-1] == 0:
				queue.append((i,j-1,step+1))
				visited1.add((i,j-1))
			if j < col-1 and (i,j+1) not in visited1 and A[i][j+1] == 0:
				queue.append((i,j+1,step+1))
				visited1.add((i,j+1))
				# dfs
		min_step = 101
		print(queue)
		while queue:
			i, j, step = queue.pop()
			if (i > 0 and A[i - 1][j] == 2) or (i < row - 1 and A[i + 1][j] == 2) \
						or ( j > 0 and A[i][j-1] == 2) or (j<col-1 and A[i][j+1]==2):
				print(step)
				min_step = min(min_step,step)
				continue
			if i > 0 and (i - 1, j) not in visited1 and A[i - 1][j] == 0:
				queue.append((i-1,j,step+1))
				visited1.add((i-1,j))
				continue
			if i < row -1 and (i+1,j) not in visited1 and A[i+1][j] == 0:
				queue.append((i+1,j,step+1))
				visited1.add((i+1,j))
				continue
			if j > 0 and (i,j-1) not in visited1 and A[i][j-1] == 0:
				queue.append((i,j-1,step+1))
				visited1.add((i,j-1))
				continue
			if j < col-1 and (i,j+1) not in visited1 and A[i][j+1] == 0:
				queue.append((i,j+1,step+1))
				visited1.add((i,j+1))
				continue
		print(min_step)

a = Solution()
print(a.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
print(a.shortestBridge([[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]))

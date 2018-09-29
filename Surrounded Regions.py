class Solution(object):
	def solve(self, board):
		"""
		给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
		找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
		--
		X X X X  运行你的函数后，矩阵变为：X X X X
		X O O X						  X X X X
		X X O X                       X X X X
		X O X X						  X O X X
		---
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		row = len(board)
		col = len(board[0])
		visited = [[0]*col for _ in range(row)]
		print(visited)
		def helper(i,j):
			print(i,j,visited)
			visited[i][j] = 1
			# 上
			if i-1>=0 and  visited[i-1][j] == 0 and board[i-1][j]== "O":
				helper(i-1,j)
			if i+1<row and visited[i+1][j]==0 and board[i+1][j] == "O":
				helper(i+1,j)
			if j-1 >= 0 and visited[i][j-1]==0 and board[i][j-1] == "O":
				helper(i,j-1)
			if j+1 < col and visited[i][j+1]==0 and board[i][j+1] == "O":
				helper(i,j+1)
		for i in range(col):
			if board[0][i] == "O":
				helper(0,i)
			if board[row-1][i] == "O":
				helper(row-1,i)
		for j in range(row):
			if board[j][0] == "O":
				helper(j,0)
			if board[j][col-1] == "O":
				helper(j,col-1)

		for i in range(1,row-1):
			for j in range(1,col-1):
				if visited[i][j] == 0 and board[i][j] == "O":
					board[i][j] = "X"

		return board
a = Solution()
# print(a.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(a.solve([["O","O"],["O","O"]]))

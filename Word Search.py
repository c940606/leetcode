class Solution:
	def exist(self, board, word):
		"""
		给定一个二维网格和一个单词，找出该单词是否存在于网格中。
		单词必须按照字母顺序，通过相邻的单元格内的字母构成，
		其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
		---
		board =
			[
			  ['A','B','C','E'],
			  ['S','F','C','S'],
			  ['A','D','E','E']
			]

			给定 word = "ABCCED", 返回 true.
			给定 word = "SEE", 返回 true.
			给定 word = "ABCB", 返回 false.
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		self.m = len(board)
		self.n = len(board[0])
		for i in range(self.m):
			for j in range(self.n):
				visited = [[0]*self.n for _ in range(self.m)]

				if self.dfs(visited,board,i,j,word,0):
					return True
		return False


	def dfs(self,visited,board,i,j,word,index):
			if index == len(word):
				return True
			if i < 0 or i > self.m-1 or j < 0 or j > self.n -1:
				return False
			if word[index] == board[i][j] and visited[i][j] == 0:
				visited[i][j] = 1
				right = self.dfs(visited,board,i+1,j,word,index+1)
				left = self.dfs(visited,board,i-1,j,word,index+1)
				up = self.dfs(visited,board,i,j+1,word,index+1)
				down = self.dfs(visited,board,i,j-1,word,index+1)
				visited[i][j] = right or left or up or down
				return left or right or up or down
			return False

	def exist1(self, board, word):
		m = len(board)
		n = len(board[0])
		print(board)
		visied = [[1]*n for _ in range(m)]
		print(visied)
		def helper(i,j,word):
			if word == "":
				return True
			visied[i][j] = 0
			if i > 0 and visied[i-1][j] and board[i-1][j] == word[0]:
				if helper(i-1,j,word[1:]):
					return True
			if i < m-1 and visied[i+1][j] and board[i+1][j] == word[0]:
				if helper(i+1,j,word[1:]):
					return True
			if j > 0 and visied[i][j-1] and board[i][j-1] == word[0]:
				if helper(i,j-1,word[1:]):
					return True
			if j < n-1 and visied[i][j+1] and  board[i][j+1] == word[0]:
				if helper(i,j+1,word[1:]):
					return True
			visied[i][j] = 1
			return False
		for i in range(m):
			for j in range(n):
				if word[0] == board[i][j]:
					print(i,j)
					if helper(i,j,word[1:]):
						return True
		return False













					# def dfs(board, used, row, col, x, y, word, idx):
		# 	if idx == len(word):
		# 		return 1
		#
		# 	if x < 0 or x > row - 1 or y < 0 or y > col - 1:
		# 		return 0
		#
		# 	if board[x][y] == word[idx] and  used[x][y]==0:
		# 		used[x][y] = 1
		# 		left = dfs(board, used, row, col, x - 1, y, word, idx + 1)
		# 		print(used)
		# 		right = dfs(board, used, row, col, x + 1, y, word, idx + 1)
		# 		print(used)
		# 		up = dfs(board, used, row, col, x, y - 1, word, idx + 1)
		# 		print(used)
		# 		down = dfs(board, used, row, col, x, y + 1, word, idx + 1)
		#
		# 		used[x][y] = left or right or up or down
		# 		print(used)
		# 		return left or right or up or down
		# 	return False
		#
		# row = len(board)
		# col = len(board[0]) if row else 0
		#
		#
		# for i in range(row):
		# 	for j in range(col):
		# 		used = [[0 for i in range(col)] for j in range(row)]
		# 		# print(used)
		# 		if dfs(board, used, row, col, i, j, word, 0):
		# 			return True
		# return False

		# class Solution:
		# 	def exist(self, board, word):
		# 		"""
		# 		:type board: List[List[str]]
		# 		:type word: str
		# 		:rtype: bool
		# 		"""
		# 		if word == "":
		# 			return True
		# 		if len(board) == 0:
		# 			return False
		# 		visited = [[0] * len(board[0]) for i in range(0, len(board))]
		# 		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		#
		# 		def dfs(i, j, board, visited, word, index):
		# 			if word[index] != board[i][j]:
		# 				return False
		# 			if len(word) - 1 == index:
		# 				return True
		# 			for direction in directions:
		# 				ni, nj = i + direction[0], j + direction[1]
		# 				if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]):
		# 					if visited[ni][nj] == 0:
		# 						visited[ni][nj] = 1
		# 						if dfs(ni, nj, board, visited, word, index + 1):
		# 							return True
		# 						visited[ni][nj] = 0
		# 			return False
		#
		# 		for i in range(0, len(board)):
		# 			for j in range(0, len(board[0])):
		# 				visited[i][j] = 1
		# 				if dfs(i, j, board, visited, word, 0):
		# 					return True
		# 				visited[i][j] = 0
		# 		return False



a = Solution()
board =			[
			  ['A','B','C','E'],
			  ['S','F','C','S'],
			  ['A','D','E','E']
			]
board1 = [["a"]]
board2 = [["w","m","y","j","s","u","x","v","t","d","f","x","p","p","m","g","j","p","i","f","i","n","s","j","e","f","t","e","g","m","x","e","a","x","o","v","s","n","s","n","s","x","k","i","o","x","q","x","o","y","e","w","l","w","i","r","d","d","x","k","p","w","q","s","t","e","n","n","t","f","a","m","c","l","u","s","k","k","r","a","k","w","w","x","u","g","o","y","j","l","k"],["b","h","a","t","c","f","g","q","y","n","q","m","r","d","g","j","p","s","a","p","e","w","o","b","r","u","r","p","g","e","z","h","n","z","c","q","g","k","g","h","x","y","t","o","e","c","x","t","w","x","l","d","u","z","e","n","v","y","c","d","c","d","m","q","c","o","i","l","y","q","s","x","q","n","l","u","p","i","q","o","i","b","r","e","c","v","r","z","v","v","d"],["y","y","p","q","a","g","a","n","e","q","f","e","g","t","p","d","k","a","t","y","i","w","p","o","a","n","f","z","i","c","c","i","a","u","a","c","a","a","q","g","q","v","k","z","q","c","c","b","c","v","z","m","t","r","a","t","e","h","s","o","j","x","x","l","t","z","n","v","a","d","b","s","b","o","r","t","q","v","u","u","s","w","g","l","n","i","e","t","p","z","h"],["a","y","g","l","t","g","a","o","g","e","r","a","h","f","u","a","x","p","x","r","i","v","x","t","k","f","a","d","w","b","m","y","b","t","l","u","b","m","k","j","s","b","j","z","h","d","b","e","v","a","w","d","x","v","y","h","d","a","m","b","d","b","a","e","u","n","a","x","z","k","g","r","m","r","s","v","x","w","b","s","y","z","v","w","v","v","f","a","w","s","b"],["z","t","d","g","p","r","g","o","s","t","u","m","f","l","e","c","k","c","d","c","b","d","z","z","a","v","e","c","r","y","d","s","r","j","y","i","a","h","w","u","a","s","g","h","g","n","j","q","p","o","t","s","t","s","r","t","p","y","v","g","w","b","z","o","k","z","y","m","g","v","g","g","p","n","n","v","a","y","m","r","n","h","k","g","z","d","c","p","b","z","x"],["y","c","y","o","o","y","o","a","g","l","j","n","b","y","c","w","a","b","i","r","q","r","d","y","r","j","c","i","k","c","h","k","g","g","y","v","g","p","v","m","a","g","b","b","e","e","y","g","h","i","a","z","a","d","x","t","o","a","d","z","e","k","l","k","s","m","f","a","b","d","n","b","j","q","d","q","u","b","w","d","l","w","c","n","c","c","g","q","e","j","r"],["i","w","d","u","o","r","c","p","s","f","e","t","q","u","w","i","r","z","f","w","n","d","z","a","h","d","h","a","h","s","r","r","o","w","n","f","n","p","w","f","w","a","b","p","w","x","x","n","z","e","k","m","i","l","m","p","o","v","p","x","o","j","q","e","h","d","j","v","v","f","c","r","h","d","i","e","d","g","t","e","k","f","q","u","q","e","m","g","c","d","f"],["q","o","v","w","w","b","i","t","w","n","v","p","x","b","y","d","e","g","w","i","s","c","a","n","u","g","b","d","i","e","i","a","v","g","x","r","h","f","k","d","u","h","u","r","i","s","w","o","y","t","y","r","x","a","g","t","h","h","w","p","n","h","q","i","n","p","b","w","u","l","z","q","v","t","k","f","o","g","u","o","b","u","f","y","v","n","s","c","u","q","t"],["k","x","j","s","k","a","w","i","w","j","h","n","e","d","z","k","t","f","g","h","h","a","p","h","x","c","z","z","z","q","t","j","p","e","d","c","h","z","k","d","j","s","s","p","x","r","b","q","x","h","z","g","k","o","n","h","r","p","j","q","f","e","z","u","k","e","w","r","e","h","v","p","b","n","e","a","h","g","s","g","p","r","m","b","g","z","l","z","o","w","p"],["v","a","q","s","k","u","q","e","a","z","b","p","a","q","w","c","x","e","w","d","t","o","p","x","w","r","i","v","h","g","m","d","g","c","x","s","y","n","y","z","n","z","q","p","q","m","u","n","q","q","t","m","e","k","l","c","b","v","x","l","b","l","q","h","n","n","b","m","a","a","l","p","z","d","h","r","q","b","h","i","r","a","w","y","k","h","a","o","c","a","z"],["d","l","p","m","b","c","o","p","e","q","c","w","r","f","d","j","v","e","s","g","x","s","c","v","e","k","y","s","m","a","t","s","n","k","e","o","o","u","d","t","k","f","r","c","l","w","n","i","c","f","o","z","z","r","x","f","d","v","a","r","x","t","j","k","e","q","z","s","k","e","n","v","m","g","z","z","c","o","h","e","v","y","e","w","r","b","b","u","y","b","n"],["v","x","z","h","b","p","g","v","z","n","l","w","z","r","x","y","u","l","h","a","i","f","e","e","y","h","g","u","h","j","i","e","g","h","m","h","w","u","f","x","h","q","u","i","h","t","i","d","h","q","e","p","x","k","w","y","u","c","s","b","l","c","i","s","j","u","b","h","q","g","f","y","y","b","i","i","u","r","l","b","j","r","t","i","e","p","i","y","t","b","b"],["e","d","j","y","p","f","c","w","w","k","d","w","j","e","e","r","b","x","e","e","i","w","x","t","a","o","b","a","h","e","d","o","k","n","o","z","u","q","v","s","b","b","o","k","f","v","d","i","u","h","n","f","f","m","y","f","b","b","h","i","i","l","y","s","a","n","r","u","d","o","p","g","p","d","q","x","a","v","f","x","d","s","c","i","h","c","q","i","d","z","s"],["n","k","r","f","k","e","w","h","j","n","w","q","e","b","i","b","e","e","j","b","j","d","d","r","k","f","j","s","k","j","n","y","t","e","f","g","k","c","p","v","r","n","l","v","o","w","z","s","c","i","t","l","n","y","e","y","f","o","s","s","z","f","s","u","j","x","c","v","b","r","r","s","e","e","q","v","c","p","p","e","z","l","p","m","j","w","m","r","m","f","j"],["l","k","d","h","w","a","k","r","c","d","k","w","k","r","m","f","t","d","w","y","c","h","p","r","t","l","d","m","z","k","v","m","x","y","u","t","a","g","m","c","j","z","b","v","q","n","c","j","r","z","j","v","i","z","o","b","m","u","n","m","e","k","y","b","k","u","w","n","a","l","r","m","k","s","h","a","g","k","l","z","l","v","w","t","u","l","x","i","f","k","u"],["l","x","v","p","j","r","l","w","s","w","o","g","g","g","p","i","o","b","u","p","m","r","m","g","l","x","d","v","e","p","s","p","o","n","e","a","g","s","w","a","q","m","g","z","v","w","h","l","z","d","b","m","u","n","u","h","m","z","d","s","q","v","h","f","k","o","f","q","i","d","r","y","s","x","x","p","v","f","c","x","k","d","j","f","s","f","m","g","e","r","y"],["u","m","i","b","y","y","i","p","g","o","g","e","i","f","c","x","d","j","z","a","t","f","l","a","z","q","p","g","u","g","g","q","v","o","s","t","o","c","i","u","q","q","b","y","w","f","x","b","o","z","b","j","e","m","k","d","c","b","l","y","h","s","o","e","i","i","a","z","l","k","t","d","b","w","e","z","b","b","a","p","a","d","b","e","p","n","k","t","o","x","t"],["x","p","j","c","a","s","c","z","f","m","u","k","p","r","o","o","u","q","q","m","s","t","n","z","k","a","j","f","o","g","y","l","y","i","p","a","c","t","z","j","i","v","v","x","o","k","o","j","c","e","v","u","a","i","t","m","k","c","s","y","l","s","l","l","c","b","l","g","w","m","r","e","j","n","e","y","x","s","h","z","y","e","v","y","o","p","l","y","t","f","w"],["g","z","j","r","c","m","e","k","j","q","c","p","c","p","t","a","o","l","j","n","k","n","k","k","b","z","x","z","t","e","x","b","e","g","t","g","v","x","s","e","q","u","t","s","j","n","u","x","a","d","m","k","s","x","x","v","y","u","w","t","z","v","v","d","d","q","l","y","p","d","c","h","a","y","b","j","n","v","j","n","a","x","a","u","w","x","p","x","t","n","q"],["s","i","n","x","m","d","k","k","t","q","p","a","q","p","c","b","c","z","m","r","c","k","t","w","i","s","o","f","o","b","w","g","m","j","g","y","p","s","k","i","i","b","k","y","q","o","c","u","o","o","o","q","y","h","o","j","c","c","o","q","g","m","y","s","y","g","s","n","z","c","x","h","g","h","i","w","y","k","t","m","y","h","e","z","q","s","i","u","x","w","m"],["d","l","l","v","j","r","n","w","q","r","t","a","x","c","k","w","a","u","p","o","u","y","u","t","q","p","b","l","m","a","x","p","l","k","m","u","e","b","s","w","s","n","w","q","p","g","o","q","c","d","g","x","d","b","q","t","q","u","g","e","w","g","v","j","s","j","f","w","k","x","t","c","k","p","u","z","y","i","r","a","n","a","z","q","b","q","m","t","m","u","z"],["k","a","w","t","t","f","y","p","p","v","i","t","h","a","o","i","a","y","c","a","m","c","a","e","f","s","q","a","g","l","z","s","n","x","l","g","c","l","y","r","i","i","m","p","k","a","x","k","b","z","n","n","d","p","t","i","j","k","i","p","x","j","h","k","g","u","t","i","f","t","b","n","b","o","e","m","q","d","w","r","f","l","g","i","a","c","r","j","o","b","a"],["l","n","j","x","t","d","q","e","k","l","h","z","n","x","d","b","q","h","z","j","m","l","s","u","l","u","n","v","i","r","x","v","e","h","s","z","k","l","f","v","w","n","u","l","m","a","m","c","h","m","m","v","x","e","r","k","y","f","h","i","w","f","d","a","m","v","b","y","g","h","t","f","u","q","q","g","q","d","j","z","r","x","w","q","b","n","a","b","s","k","j"],["q","p","m","s","b","h","u","b","q","b","v","v","v","n","l","d","f","o","o","g","h","l","c","x","m","p","y","n","k","i","w","a","z","i","t","c","s","p","d","i","q","a","d","n","p","q","s","u","f","h","c","o","s","e","m","h","w","m","w","g","u","v","i","v","f","d","x","x","s","a","h","i","d","k","x","s","b","q","n","i","x","r","w","r","w","k","a","s","w","x","a"],["q","u","i","n","z","m","k","z","g","n","g","p","s","t","m","k","w","e","z","g","b","r","e","v","p","p","v","h","l","u","j","e","q","t","r","q","f","e","r","m","r","z","d","j","s","r","v","q","w","v","w","z","m","b","u","d","q","s","m","b","m","v","f","d","o","x","v","w","d","o","k","u","n","p","f","g","g","c","w","e","x","v","e","l","w","a","o","o","s","a","p"],["f","x","x","k","m","w","h","k","z","v","u","v","i","j","c","q","r","e","p","w","c","k","c","p","g","c","g","w","v","g","l","c","g","i","m","s","g","t","e","f","o","y","a","y","j","c","p","c","h","e","a","l","q","e","c","y","h","i","u","e","r","f","g","x","q","u","r","w","p","v","e","f","v","e","d","g","j","u","k","s","y","l","f","o","p","h","m","y","s","g","c"],["j","o","k","i","g","e","z","e","v","w","i","a","t","p","g","z","y","a","l","s","z","y","x","p","o","g","e","o","y","m","t","j","c","d","r","i","k","s","n","f","q","v","i","j","k","o","k","k","o","w","c","p","u","z","h","k","i","l","b","g","z","u","q","c","z","j","k","j","e","z","r","u","v","b","e","h","r","q","s","f","o","w","x","l","y","e","v","g","r","y","m"],["q","s","e","s","u","o","f","d","s","e","w","o","b","z","u","l","q","l","f","y","z","b","v","m","b","b","i","h","s","i","w","k","b","a","f","v","q","m","a","k","s","z","z","u","y","t","h","r","g","m","p","i","p","k","u","r","n","e","a","h","n","w","r","q","z","y","n","p","k","p","c","d","o","b","z","p","w","g","g","f","s","v","n","j","h","h","a","u","o","b","b"],["b","x","u","r","y","t","g","q","d","v","s","i","m","v","h","b","t","n","j","y","h","g","l","r","p","v","t","l","j","u","m","k","u","i","d","s","b","l","i","h","g","c","p","s","x","z","v","r","o","g","p","y","m","d","p","b","y","k","m","h","f","a","t","b","l","y","t","o","l","e","v","r","g","n","m","e","o","j","x","c","q","o","a","e","r","r","g","r","c","u","a"],["j","x","v","k","i","t","f","w","e","j","u","y","q","j","m","w","x","v","v","b","l","j","c","s","d","v","a","u","x","u","v","i","t","q","s","d","m","y","c","s","h","y","s","z","h","e","x","e","c","s","h","p","e","j","h","h","h","h","d","e","e","a","n","x","t","h","d","h","f","f","b","p","d","u","q","m","a","o","s","c","i","z","s","m","l","b","v","s","j","z","y"],["n","z","l","k","u","v","p","b","a","w","d","p","z","x","g","n","z","w","f","e","e","h","w","t","s","x","o","k","i","p","i","v","r","w","i","l","t","x","n","t","u","s","l","v","p","t","j","q","r","q","u","v","z","s","q","r","s","h","d","a","w","o","w","p","m","g","b","f","d","q","a","z","i","n","v","z","g","g","r","x","y","m","v","y","e","l","r","w","s","x","z"],["r","n","v","g","z","b","j","g","g","b","g","g","l","u","d","k","c","l","c","c","l","q","z","j","u","k","d","t","f","c","s","y","p","p","e","o","s","q","w","a","r","e","i","d","a","l","p","d","y","t","h","k","j","g","t","g","q","y","z","x","a","t","v","p","k","c","f","e","u","d","e","l","i","n","q","i","a","g","n","z","z","u","j","l","a","e","r","t","f","s","q"],["f","n","o","x","x","s","e","b","m","i","h","x","q","u","q","a","x","w","o","w","x","i","f","i","l","l","b","e","q","t","w","y","g","m","v","f","e","z","i","q","h","q","q","z","m","g","c","j","e","q","h","b","a","o","m","n","a","n","r","q","j","q","o","p","c","l","x","h","l","f","z","u","v","p","w","k","x","y","v","d","q","d","h","s","r","t","g","r","i","x","k"],["r","n","a","j","q","o","g","z","b","l","y","v","j","q","t","v","p","t","q","t","j","t","a","c","l","v","k","e","d","h","q","x","x","r","g","p","f","m","o","g","z","o","d","k","e","z","f","w","s","w","p","e","r","r","i","e","m","s","j","r","z","z","o","y","s","w","p","z","k","f","h","k","u","n","w","a","m","c","w","g","a","l","k","t","e","s","y","q","k","j","i"],["m","k","y","m","d","v","c","e","f","h","m","r","d","b","o","e","n","s","c","v","u","q","g","n","u","a","n","l","l","w","v","z","h","v","l","m","q","n","q","y","x","e","p","a","f","f","g","u","z","j","q","v","z","w","l","t","y","y","g","j","x","d","k","e","z","w","q","r","l","i","p","i","n","h","j","s","m","p","n","o","a","f","j","z","d","u","v","b","v","d","n"],["s","j","x","w","i","t","o","z","f","y","r","p","l","y","y","g","k","q","v","a","q","a","k","s","d","g","p","e","b","u","t","t","d","r","p","n","k","f","n","r","e","e","h","r","c","h","x","o","z","u","r","s","u","b","m","z","h","d","g","j","x","z","c","b","q","u","o","d","b","d","w","h","j","f","z","n","p","y","e","q","t","v","i","p","w","w","r","f","z","x","q"],["x","y","v","a","r","r","q","u","s","u","s","c","f","y","b","t","p","b","x","f","w","s","q","m","o","m","f","v","m","c","m","j","c","h","l","t","y","b","p","q","x","i","s","d","i","v","w","z","z","t","e","v","n","u","h","d","h","o","y","v","q","k","g","v","r","r","o","p","s","e","i","s","o","c","v","w","a","r","v","z","m","b","u","z","y","e","e","h","s","c","c"],["l","n","i","g","g","z","u","y","t","a","i","l","o","k","g","m","m","z","j","l","n","l","i","o","j","o","s","q","i","v","u","t","k","c","b","q","d","y","o","y","y","w","k","p","j","s","b","x","u","n","j","h","a","t","y","l","j","q","d","r","n","x","l","z","z","o","q","e","m","g","c","n","f","o","c","q","h","f","n","d","s","y","k","s","r","k","d","a","d","g","u"],["q","d","h","q","e","v","i","k","i","q","n","v","v","b","z","n","k","e","b","n","z","z","a","r","t","k","x","v","n","f","r","g","l","y","y","p","u","i","c","e","y","p","b","w","s","a","j","f","g","m","s","f","m","u","z","h","f","w","e","u","b","w","c","m","u","c","e","q","k","g","u","j","x","v","h","r","x","q","w","e","d","p","j","r","j","k","a","q","g","g","n"],["k","e","r","y","b","u","e","r","e","m","m","p","l","j","y","d","h","r","z","l","u","q","w","n","c","h","p","u","p","v","j","b","a","b","a","d","v","g","u","b","t","i","t","e","s","r","j","b","i","j","o","e","b","k","t","f","t","i","a","j","g","j","k","g","k","m","j","h","t","f","l","o","o","e","s","i","x","c","l","i","n","z","o","q","l","i","w","f","s","y","o"],["y","h","y","g","u","n","r","d","g","x","o","u","n","s","o","x","s","s","k","c","h","j","q","y","u","a","u","z","t","u","p","r","b","q","a","x","d","r","b","l","q","p","h","f","k","v","c","c","q","m","e","x","x","w","x","u","x","t","v","q","n","l","j","p","b","j","o","e","b","p","r","r","f","y","x","r","v","b","t","l","q","z","l","p","v","i","j","s","c","f","k"],["r","q","u","g","t","d","x","z","g","m","q","y","t","o","x","k","j","a","f","v","q","g","i","g","c","q","p","w","u","w","h","m","m","b","u","f","g","r","e","n","g","w","n","b","k","m","o","u","m","v","r","d","c","b","l","g","r","c","c","o","z","l","c","n","o","w","v","v","q","b","k","y","y","x","z","k","j","p","g","x","l","z","c","n","a","n","v","u","s","z","i"],["t","l","k","i","z","i","d","w","y","h","i","y","f","h","y","r","q","n","y","q","a","x","s","p","y","g","k","s","a","k","a","t","v","m","b","w","u","h","v","v","q","d","t","x","l","t","o","d","j","m","t","j","k","o","z","i","u","l","c","w","v","e","r","s","s","u","r","m","b","m","j","t","r","f","q","e","y","f","k","j","r","d","v","d","r","u","n","n","f","p","l"],["d","v","c","v","n","x","m","a","a","a","l","u","s","s","k","y","t","r","i","c","j","m","x","m","f","t","c","v","b","r","g","e","n","l","b","a","k","q","c","k","q","q","g","k","i","t","j","b","k","r","e","t","f","d","i","n","x","k","k","y","d","s","e","s","d","h","v","n","x","z","a","q","p","g","a","y","z","l","b","m","f","h","f","k","l","p","z","k","b","j","i"],["h","c","o","z","h","v","w","x","v","w","x","l","l","f","n","l","h","z","n","t","g","u","a","q","h","q","s","r","t","d","b","c","f","p","e","p","n","a","m","i","w","j","v","k","q","k","v","x","j","k","q","r","f","r","k","m","j","c","g","e","f","h","h","n","z","l","c","m","l","q","w","k","b","t","u","r","d","p","p","p","a","f","g","h","w","q","v","h","s","b","m"],["a","j","t","n","i","e","r","w","r","h","u","b","k","n","v","b","q","n","q","h","n","w","o","w","u","e","t","c","z","v","o","b","g","j","o","q","n","h","m","e","q","i","i","a","v","d","b","n","q","s","v","f","q","l","d","m","r","x","o","s","s","e","t","a","n","j","q","c","q","c","j","g","k","r","g","h","w","k","w","n","e","t","u","u","e","y","g","y","x","x","q"],["p","d","k","p","t","t","h","v","m","j","g","s","v","z","b","e","w","l","a","l","p","u","f","l","a","f","t","y","c","q","r","t","w","b","k","p","w","r","m","i","c","t","d","z","u","e","d","q","r","g","b","i","c","j","v","e","o","o","d","t","h","u","m","d","x","x","u","v","o","g","e","r","b","h","q","w","n","w","o","e","c","q","o","g","z","j","k","p","z","p","i"],["g","j","v","l","i","u","f","e","k","o","k","b","r","r","u","p","g","q","e","k","u","w","a","a","v","j","k","m","i","a","v","r","l","s","e","w","m","k","c","w","a","m","a","t","f","w","j","l","o","p","x","i","l","x","k","i","i","w","u","s","y","p","j","m","j","o","i","x","a","m","w","c","a","w","x","f","u","g","s","i","x","p","q","k","o","c","s","w","y","n","o"],["x","e","a","l","q","q","t","n","s","h","j","w","h","h","t","m","b","c","e","l","z","v","b","k","j","f","c","h","e","r","x","d","y","x","o","o","p","j","d","h","s","n","d","z","w","z","n","a","b","r","l","a","o","p","m","z","u","r","g","a","i","d","f","i","d","v","w","u","e","a","e","w","p","j","x","l","i","k","n","j","d","z","m","r","o","y","q","k","p","y","l"],["a","e","s","i","j","o","f","f","u","h","j","r","w","t","q","j","d","b","x","n","e","w","b","y","m","z","q","w","p","p","j","p","v","c","z","g","q","e","l","k","l","v","d","j","q","w","t","t","x","q","i","d","o","j","b","a","l","s","y","c","j","k","t","g","m","s","m","e","x","x","q","k","s","w","u","k","s","n","e","r","f","o","u","t","a","w","v","l","q","t","n"],["z","d","i","f","r","a","t","v","z","q","o","k","l","m","g","v","g","v","b","x","a","q","t","v","s","p","q","d","h","j","s","g","p","a","n","g","a","g","e","a","z","s","m","k","g","s","f","m","p","j","l","p","b","e","k","t","w","a","y","d","l","s","m","a","s","z","h","u","i","n","w","j","h","k","t","n","e","a","z","t","l","m","k","m","q","u","h","m","w","f","q"],["k","x","c","k","r","d","t","o","n","g","k","w","n","x","r","c","b","u","d","v","f","p","f","s","g","c","z","u","a","h","k","k","g","o","x","y","u","q","m","h","z","y","g","o","v","z","r","x","t","u","u","z","k","b","t","s","d","u","m","g","d","z","q","k","n","n","i","h","g","w","r","h","u","x","v","q","w","o","p","s","j","l","t","t","m","m","n","s","i","z","y"],["m","y","q","w","o","g","e","v","m","a","o","v","w","l","s","o","k","h","f","e","q","q","x","l","f","j","y","x","t","x","x","f","y","n","d","m","t","j","j","h","l","y","e","i","l","x","w","v","e","e","b","w","u","y","h","b","j","h","a","d","g","x","k","e","n","o","q","g","x","a","q","j","y","u","t","j","r","p","h","x","v","i","t","q","j","c","r","s","j","u","v"],["q","r","g","u","e","u","n","n","t","p","d","e","p","x","x","y","r","p","h","o","k","s","k","a","b","m","u","t","w","o","r","o","h","x","k","o","t","x","b","o","m","g","t","b","f","q","c","w","f","l","n","q","d","x","s","g","l","o","c","j","e","t","x","o","s","i","c","n","h","f","b","w","l","u","z","s","n","b","p","u","p","e","k","u","d","f","b","o","v","d","y"],["a","y","x","o","q","h","s","d","p","x","e","l","k","b","k","c","q","o","t","k","d","x","v","z","a","c","a","r","x","f","r","z","d","o","n","v","y","h","y","n","g","f","a","q","i","m","v","y","c","q","i","h","o","f","h","q","h","j","j","h","r","a","g","u","r","w","q","p","d","q","e","k","v","g","c","f","u","z","d","x","q","m","g","g","r","p","w","b","z","i","i"],["q","i","o","m","b","k","e","s","q","v","y","c","s","e","g","y","b","g","d","a","w","p","g","c","j","w","a","m","x","k","u","p","v","k","b","w","x","g","r","n","d","p","p","v","w","v","v","x","d","z","z","z","q","h","d","b","d","g","n","c","q","h","r","n","u","v","k","r","b","d","e","g","s","v","d","q","q","z","p","u","a","o","v","s","w","b","u","b","j","h","e"],["b","r","x","p","l","s","b","c","v","e","g","b","y","d","f","p","t","g","e","p","i","v","n","a","r","o","u","u","z","c","a","a","t","y","r","e","s","s","i","o","y","q","p","x","t","w","o","o","e","u","e","m","p","t","n","i","h","h","d","i","l","d","i","e","d","c","k","w","u","s","k","v","i","b","s","d","y","i","s","c","c","y","r","u","r","e","e","a","n","h","i"],["z","n","s","d","q","u","q","m","p","k","w","k","v","a","e","y","y","o","q","c","s","o","t","m","f","z","t","f","n","a","n","m","n","i","r","g","c","h","s","t","s","r","d","p","r","j","n","r","x","e","t","s","u","p","g","c","o","z","h","d","a","x","r","p","f","j","v","j","s","q","d","m","h","i","b","y","s","p","r","r","v","k","j","p","b","q","t","s","r","b","v"],["r","a","n","j","h","y","g","q","q","w","t","d","f","e","g","f","w","v","w","p","s","j","b","k","k","t","d","e","k","e","a","e","g","p","n","p","p","v","g","f","s","b","k","z","f","r","f","d","o","b","v","h","m","w","r","x","r","u","d","b","b","d","f","j","u","u","z","l","q","h","r","k","i","d","j","q","w","o","t","n","s","q","w","g","m","n","f","d","j","j","h"]]
board3 =[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","b"]]
print(a.exist1(board,"SEE"))





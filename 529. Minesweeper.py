# class Solution(object):
# 	def updateBoard2(self, board, click):
# 		"""
# 		:type board: List[List[str]]
# 		:type click: List[int]
# 		:rtype: List[List[str]]
# 		"""
# 		from collections import defaultdict
# 		dilei = defaultdict(int)
# 		orients = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
# 		visited = set()
# 		row = len(board)
# 		col = len(board[0])
# 		for i in range(row):
# 			for j in range(col):
# 				if board[i][j] == "M":
# 					for x, y in orients:
# 						if 0 <= i + x < row and 0 <= j + y < col:
# 							dilei[(i + x, j + y)] += 1
#
# 		def dfs(click_i, click_j):
# 			visited.add((click_i, click_j))
# 			if board[click_i][click_j] == "M":
# 				board[click_i][click_j] = "X"
# 				return
# 			if (click_i, click_j) in dilei:
# 				board[click_i][click_j] = str(dilei[(click_i, click_j)])
# 				return
# 			if board[click_i][click_j] == "E":
# 				board[click_i][click_j] = "B"
# 			for x, y in orients:
# 				X = click_i + x
# 				Y = click_j + y
# 				if 0 <= X < row and 0 <= Y < col and (X, Y) not in visited:
# 					dfs(X, Y)
#
# 		dfs(*click)
# 		return board
#
# 	def updateBoard1(self, board, click):
# 		from collections import defaultdict, deque
# 		dilei = defaultdict(int)
# 		orients = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
# 		visited = set()
# 		stack = deque()
# 		stack.appendleft(click)
# 		row = len(board)
# 		col = len(board[0])
# 		for i in range(row):
# 			for j in range(col):
# 				if board[i][j] == "M":
# 					for x, y in orients:
# 						if 0 <= i + x < row and 0 <= j + y < col:
# 							dilei[(i + x, j + y)] += 1
# 		while stack:
# 			x, y = stack.pop()
# 			visited.add((x, y))
# 			if board[x][y] == "M":
# 				board[x][y] = "X"
# 				break
# 			if (x, y) in dilei:
# 				board[x][y] = str(dilei[(x, y)])
# 				continue
# 			if board[x][y] == "E":
# 				board[x][y] = "B"
# 				for i, j in orients:
# 					X = x + i
# 					Y = y + j
# 					if 0 <= X < row and 0 <= Y < col and (X, Y) not in visited:
# 						stack.appendleft([X, Y])
#
# 		return board
#
# 	def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
# 		i, j = click
# 		row, col = len(board), len(board[0])
# 		if board[i][j] == "M":
# 			board[i][j] = "X"
# 			return board
#
# 		# 计算空白快周围的地雷
# 		def cal(i, j):
# 			res = 0
# 			for x in [1, -1, 0]:
# 				for y in [1, -1, 0]:
# 					if x == 0 and y == 0: continue
# 					if 0 <= i + x < row and 0 <= j + y < col and board[i + x][j + y] == "M": res += 1
# 			return res
#
# 		def dfs(i, j):
# 			num = cal(i, j)
# 			if num > 0:
# 				board[i][j] = str(num)
# 				return
# 			board[i][j] = "B"
# 			for x in [1, -1, 0]:
# 				for y in [1, -1, 0]:
# 					if x == 0 and y == 0: continue
# 					nxt_i, nxt_j = i + x, j + y
# 					if 0 <= nxt_i < row and 0 <= nxt_j < col and board[nxt_i][nxt_j] == "E": dfs(nxt_i, nxt_j)
#
# 		dfs(i, j)
# 		return board


print('\n'.join([''.join([('****'[(x - y) % 4] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
		y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))

res = []

for y in range(15, -15, -1):
	tmp = []
	for x in range(-30, 30):
		if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
			tmp.append('*')
		else:
			tmp.append(" ")
	res.append("".join(tmp))
print("\n".join(res))


# a = Solution()
# print(a.updateBoard1([['E', 'E', 'E', 'E', 'E'],
# 					  ['E', 'E', 'M', 'E', 'E'],
# 					  ['E', 'E', 'E', 'E', 'E'],
# 					  ['E', 'E', 'E', 'E', 'E']], [3, 0]))
# print(a.updateBoard1([['B', '1', 'E', '1', 'B'],
# 					  ['B', '1', 'M', '1', 'B'],
# 					  ['B', '1', '1', '1', 'B'],
# 					  ['B', 'B', 'B', 'B', 'B']], [1, 2]))
# print(a.updateBoard1([["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
# 					  ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
# 					   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"]]
# 					 , [29, 2]))

class Solution(object):
	def countBattleships(self, board):
		"""
		给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：
		给你一个有效的甲板，仅由战舰或者空位组成。
		战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
		两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰
		---
		X..X
		...X
		...X
		:type board: List[List[str]]
		:rtype: int
		"""
		row = len(board)
		col = len(board[0])
		res = 0
		for i in range(row):
			for j in range(col):
				if i == 0 and j == 0 and board[i][j] == "X":
					res += 1
				elif i == 0 and board[i][j] == "X" and  board[i][j-1] == ".":
					res += 1
				elif j == 0 and board[i][j] == "X" and  board[i-1][j] == ".":
					res += 1
				elif board[i][j] == "X" and (board[i-1][j] == ".") and ( board[i][j-1]=="."):
					print(i,j)
					res += 1
		return res
a = Solution()
print(a.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print(a.countBattleships([["X","X","X"]]))
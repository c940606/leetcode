import copy
class Solution(object):
	def gameOfLife1(self, board):
		"""
		根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。
		给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或 dead（0）即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
		如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
		如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
		如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
		如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
		根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
		----
		示例:
		输入:
		[
		  [0,1,0],
		  [0,0,1],
		  [1,1,1],
		  [0,0,0]
		]
		输出:
		[
		  [0,0,0],
		  [1,0,1],
		  [0,1,1],
		  [0,1,0]
		]
		---
		思路:

		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		self.row = len(board)
		self.col = len(board[0])
		self.flag = copy.deepcopy(board)
		for s in range(self.row):
			for k in range(self.col):
				num = self.helper_count_live(s, k)
				if board[s][k] == 1:
					if num < 2 or num > 3:
						board[s][k] = 0
				else:
					if num == 3:
						board[s][k] = 1

	def helper_count_live(self,i, j):
		count_live = 0
		if i - 1 >= 0 and j - 1 >= 0 and self.flag[i - 1][j - 1] == 1:
			count_live += 1
		if j - 1 >= 0 and self.flag[i][j - 1] == 1:
			count_live += 1
		if i + 1 < self.row and j - 1 >= 0 and self.flag[i + 1][j - 1] == 1:
			count_live += 1
		if i - 1 >= 0 and self.flag[i - 1][j] == 1:
			count_live += 1
		if i + 1 < self.row and self.flag[i + 1][j] == 1:
			count_live += 1
		if i - 1 >= 0 and j + 1 < self.col and self.flag[i - 1][j + 1] == 1:
			count_live += 1
		if j + 1 < self.col and self.flag[i][j + 1] == 1:
			count_live += 1
		if i + 1 < self.row and j + 1 < self.col and self.flag[i + 1][j + 1] == 1:
			count_live += 1
		return count_live

	def gameOfLife(self, board):
		"""
		:param board:
		:return:
		"""



a = Solution()
print(a.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))

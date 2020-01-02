from pprint import pprint
from typing import List


class Solution1:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        from copy import deepcopy
        row = len(board)
        col = len(board[0])

        def repeated(board):
            res = deepcopy(board)
            flag = False
            # 行
            for i in range(row):
                for j in range(col - 2):
                    if board[i][j] == 0: continue
                    if board[i][j] == board[i][j + 1] == board[i][j + 2]:
                        res[i][j] = res[i][j + 1] = res[i][j + 2] = 0
                        if not flag:
                            flag = True
            # 列
            for j in range(col):
                for i in range(row - 2):
                    if board[i][j] == 0: continue
                    if board[i][j] == board[i + 1][j] == board[i + 2][j]:
                        res[i][j] = res[i + 1][j] = res[i + 2][j] = 0
                        if not flag:
                            flag = True
            return flag, res

        def sink(board):
            res = [[0] * col for _ in range(row)]

            for j in range(col):
                loc = row - 1
                for i in range(row - 1, -1, -1):
                    if board[i][j] == 0: continue
                    res[loc][j] = board[i][j]
                    loc -= 1
            return res

        flag, board = repeated(board)
        while flag:
            board = sink(board)
            flag, board = repeated(board)
        return board


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        :arg
        1. 把所有可以消除的置0
        2. 下沉0
        3. 重复1, 2 当没有可以消除的时候
        """
        row = len(board)
        col = len(board[0])

        def repeated(board):
            del_loc = set()
            flag = False
            # 行
            for i in range(row):
                for j in range(col - 2):
                    if board[i][j] == 0: continue
                    if board[i][j] == board[i][j + 1] == board[i][j + 2]:
                        del_loc.update([(i, j), (i, j + 1), (i, j + 2)])
                        if not flag:
                            flag = True
            # 列
            for j in range(col):
                for i in range(row - 2):
                    if board[i][j] == 0: continue
                    if board[i][j] == board[i + 1][j] == board[i + 2][j]:
                        del_loc.update([(i, j), (i + 1, j), (i + 2, j)])
                        # res[i][j] = res[i + 1][j] = res[i + 2][j] = 0
                        if not flag:
                            flag = True

            if flag:
                for i, j in del_loc:
                    board[i][j] = 0
            return flag, board

        def sink(board):

            for j in range(col):
                loc = row - 1
                for i in range(row - 1, -1, -1):
                    if board[i][j] == 0: continue
                    board[loc][j], board[i][j] = board[i][j], board[loc][j]
                    loc -= 1
            return board

        flag, board = repeated(board)
        while flag:
            board = sink(board)
            flag, board = repeated(board)
        return board


a = Solution()
pprint(a.candyCrush([[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
                     [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1],
                     [1, 1, 2, 2, 2],
                     [4, 1, 4, 4, 1014]]))

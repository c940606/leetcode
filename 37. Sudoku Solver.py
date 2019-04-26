class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check(board, i, j, k):
            for t in range(9):
                if t != j and board[i][t] == k:
                    return False
                if t != i and board[t][j] == k:

                    return False
            tmp_i = i // 3 * 3
            tmp_j = j // 3 * 3
            for s in range(tmp_i, tmp_i + 3):
                for t in range(tmp_j, tmp_j + 3):
                    if s != i and t != j and board[s][t] == k:
                        return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in [str(i) for i in range(1, 10)]:
                            if check(board, i, j, k):
                                board[i][j] = k
                                if solve(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True

        solve(board)
        print(board)



if __name__ == '__main__':
    a = Solution()
    print(a.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."],
                         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

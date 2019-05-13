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

    def solveSudoku1(self, board) -> None:
        all_points = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    all_points.append((i, j))

        # print(all_points)

        def helper(board, i, j, k):
            for s in range(9):
                # hang
                if s != i and board[s][j] == k:
                    return False
                if s != j and board[i][s] == k:
                    return False

            for t in range(i // 3 * 3, i // 3 * 3 + 3):
                for q in range(j // 3 * 3, j // 3 * 3 + 3):
                    if t != i and q != j and board[t][q] == k:
                        return False
            return True

        def backtrack(board, i):
            if i == len(all_points):
                return True
            for k in range(1, 10):
                if helper(board, all_points[i][0], all_points[i][1], str(k)):
                    board[all_points[i][0]][all_points[i][1]] = str(k)
                    if backtrack(board, i + 1):
                        return True
                    board[all_points[i][0]][all_points[i][1]] = None
            return False

        backtrack(board, 0)
        print(board)

    def solveSudoku3(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_points = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    all_points.add((i, j))

        # print(all_points)
        def helper(board, i, j, k):
            for s in range(9):
                # hang
                if s != i and board[s][j] == k:
                    return False
                if s != j and board[i][s] == k:
                    return False

            for t in range(i // 3 * 3, i // 3 * 3 + 3):
                for q in range(j // 3 * 3, j // 3 * 3 + 3):
                    if t != i and q != j and board[t][q] == k:
                        return False
            return True

        def backtrack(board, all_points, visited):
            print(len(all_points), len(visited))
            print(board)
            if len(visited) == len(all_points):
                return True
            for i, j in all_points:
                if (i, j) not in visited:
                    visited.add((i, j))
                    for k in range(1, 10):

                        if helper(board, i, j, str(k)):
                            board[i][j] = str(k)

                            if backtrack(board, all_points, visited):
                                print(all_points)
                                return True
                            board[i][j] = "."
                    visited.remove((i, j))
                    return False

                    # all_points.add((i, j))
            return False

        # print(helper(board,0,2,"4"))
        backtrack(board, all_points, set())
        print(board)


if __name__ == '__main__':
    a = Solution()
    print(a.solveSudoku3([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                          [".", "9", "8", ".", ".", ".", ".", "6", "."],
                          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                          [".", "6", ".", ".", ".", ".", "2", "8", "."],
                          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

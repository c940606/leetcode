class Solution(object):
    def solve1(self, board):
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
        visited = [[0] * col for _ in range(row)]
        print(visited)

        def helper(i, j):
            print(i, j, visited)
            visited[i][j] = 1
            # 上
            if i - 1 >= 0 and visited[i - 1][j] == 0 and board[i - 1][j] == "O":
                helper(i - 1, j)
            if i + 1 < row and visited[i + 1][j] == 0 and board[i + 1][j] == "O":
                helper(i + 1, j)
            if j - 1 >= 0 and visited[i][j - 1] == 0 and board[i][j - 1] == "O":
                helper(i, j - 1)
            if j + 1 < col and visited[i][j + 1] == 0 and board[i][j + 1] == "O":
                helper(i, j + 1)

        for i in range(col):
            if board[0][i] == "O":
                helper(0, i)
            if board[row - 1][i] == "O":
                helper(row - 1, i)
        for j in range(row):
            if board[j][0] == "O":
                helper(j, 0)
            if board[j][col - 1] == "O":
                helper(j, col - 1)

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if visited[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"

        return board

    def solve3(self, board):
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][col - 1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(row):
            for j in range(col):
                if board[i][j] == "B":
                    board[i][j] = "O"
        print(board)

    def solve6(self, board):
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"
        # for i in range(row):
        #         #     for j in range(col):

        print(board)

    def solve(self, board):
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:Palindrome Partitioning II
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        print(board)

a = Solution()
print(a.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
# print(a.solve([["O", "O"], ["O", "O"]]))
print(a.solve([["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
               ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
               ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
               ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
               ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
               ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
               ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
               ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
               ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
               ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]))
print(a.solve([["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
               ["O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
               ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X"],
               ["O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O"],
               ["O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
               ["X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O"],
               ["O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O"],
               ["X", "O", "O", "O", "X", "X", "X", "O", "X", "O", "O", "O", "O", "X", "X", "O", "X", "O", "O", "O"],
               ["O", "O", "O", "O", "O", "X", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O"],
               ["X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "X", "X", "O", "O", "X", "O", "O", "X"],
               ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "X", "O", "X"],
               ["O", "O", "O", "O", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O"],
               ["X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
               ["O", "X", "O", "X", "O", "O", "O", "X", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "O", "O"],
               ["O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "X", "O"],
               ["X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "X", "X", "O", "O", "O", "X", "O", "O"],
               ["O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "X", "O", "X", "O", "O"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "X", "X", "O", "O", "X", "O", "O", "O", "X", "O"],
               ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
               ["X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "O", "O", "X", "O", "X", "O", "X", "O", "O"]]))

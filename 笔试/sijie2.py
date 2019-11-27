def maxPathSum(board, p, q):
    row = len(board)
    col = len(board[0])

    def helper1(p):
        dp = [[0] * col for _ in range(row)]
        dp[0][p] = board[0][p]
        for i in range(1, row):
            for j in range(0, col):
                if j - 1 >= 0 and dp[i - 1][j - 1]:
                    dp[i][j] = max(board[i][j] + dp[i - 1][j - 1], dp[i][j])
                if dp[i - 1][j]:
                    dp[i][j] = max(board[i][j] + dp[i - 1][j], dp[i][j])
                if j + 1 < col and dp[i - 1][j + 1]:
                    dp[i][j] = max(board[i][j] + dp[i - 1][j + 1], dp[i][j])
        return max(dp[-1])

    def helper2(q):
        dp = [[0] * col for _ in range(row)]
        dp[row - 1][q] = board[row - 1][q]
        for i in range(row - 2, -1, -1):
            for j in range(0, col):
                if j - 1 >= 0 and dp[i + 1][j - 1]:
                    dp[i][j] = max(board[i][j] + dp[i + 1][j - 1], dp[i][j])
                if dp[i + 1][j]:
                    dp[i][j] = max(board[i][j] + dp[i + 1][j], dp[i][j])
                if j + 1 < col and dp[i + 1][j + 1]:
                    dp[i][j] = max(board[i][j] + dp[i + 1][j + 1], dp[i][j])
        return max(dp[0])

    return max(helper1(p), helper2(q))


print(maxPathSum([[9, 4, 7], [2, 1, 3], [1, 4, 2]], 0, 2))
print(maxPathSum([[9, 4, 7], [2, 1, 3], [1, 4, 2]], 2, 1))
print(maxPathSum([[173, 63, 387], [413, 307, 124], [451, 127, 119]], 0, 0))

dp = [[0] * n for _ in range(m)]
# 第一行变成1
for j in range(n):
    dp[0][j] = 1
# 第一列变成1
for i in range(m):
    dp[i][0] = 1

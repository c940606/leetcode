from  pprint import pprint
def cow_num(n):
    dp = [[0] * 6 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(6):
            #print(dp)
            if j == 0:
                dp[i][j] = dp[i - 1][3] + dp[i - 1][5]
            else:
                dp[i][j] = dp[i - 1][j - 1]
    pprint(dp)
    return sum(dp[-1])
# print(cow_num(3))
print(cow_num(6))

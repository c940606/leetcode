def findMaxSubListLen(a, b):
    if not a or not b:return 0
    a_l = len(a)
    b_l = len(b)
    dp = [[0] * (b_l + 1) for _ in range(a_l + 1)]
    res = 0
    for i in range(1, a_l + 1):
        for j in range(1, b_l + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(dp[i][j], res)
    #print(res)
    return res


findMaxSubListLen([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])

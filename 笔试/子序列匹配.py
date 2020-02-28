def match(s, p):
    from collections import defaultdict
    dp = [defaultdict(int) for _ in range(len(s))]
    if s[0] == p[0]:
        dp[0][s[0]] = 1

    for i in range(1, len(s)):
        for j in range(len(p)):
            if j == 0:
                if s[i] == p[j]:
                    dp[i][p[0]] = dp[i - 1][p[0]] + 1
                continue
            if s[i] != p[j]:
                dp[i][p[:j + 1]] = dp[i - 1][p[:j + 1]]
            else:
                dp[i][p[:j + 1]] = dp[i - 1][p[:j]] +  dp[i - 1][p[:j + 1]]
    return dp[-1][p]


print(match("alleeetcode", "leetcode"))

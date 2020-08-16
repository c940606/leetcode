class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = dp[i] or not dp[i - j * j]
        return dp[-1]
a = Solution()
print(a.winnerSquareGame(17))


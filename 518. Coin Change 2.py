class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        coins.sort()
        self.res = 0

        def dfs(remain, loc):
            if remain == 0:
                self.res += 1
            else:
                for i in range(loc, n):
                    if coins[i] > remain:
                        break
                    else:
                        dfs(remain - coins[i], i)

        # for i in range(n):
        dfs(amount, 0)
        return self.res

    def change1(self, amount, coins):
        dp = [[1] + [0] * amount for _ in range(len(coins) + 1)]
        print(dp)
        n = len(coins)
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        print(dp)
        return dp[-1][-1]


a = Solution()
print(a.change1(5, [1, 2, 5]))
print(a.change(3, [2]))

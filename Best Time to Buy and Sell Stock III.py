class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        buy1 = [0] * n
        sell1 = [0] * n
        buy2 = [0] * n
        sell2 = [0] * n
        buy1[0] = -prices[0]
        buy2[0] = -prices[0]
        for i in range(1, n):
            buy1[i] = max(buy1[i - 1], -prices[i])
            sell1[i] = max(sell1[i - 1], buy1[i - 1] + prices[i])
            buy2[i] = max(buy2[i - 1], sell1[i - 1] - prices[i])
            sell2[i] = max(sell2[i - 1], buy2[i - 1] + prices[i])
        return sell2[-1]

    def maxProfit2(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            for i in range(1, n):
                for j in range(i + 1):
                    if j == 0:
                        dp[k][i] = max(dp[k][i], dp[k][i - 1], prices[i] - prices[j])
                    else:
                        dp[k][i] = max(dp[k][i], dp[k][i - 1], dp[k - 1][j - 1] + prices[i] - prices[j])
        print(dp)
        return dp[-1][-1]

    def maxProfit4(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            for i in range(1, n):
                # 处理边界情况 j == 0
                pre_max = -prices[0]
                for j in range(1, i + 1):
                    pre_max = max(pre_max, dp[k - 1][j - 1] - prices[j])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]

    def maxProfit6(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]

    def maxProfit(self, prices):
        dp = [[[0, 0] for _ in range(len(prices) + 1)] for _ in range(3)]
        for i in range(len(prices) + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = float("-inf")

        for k in range(1, 3):
            for i in range(len(prices) + 1):
                for j in range(i):
                    dp[k][i][1] = max(dp[k - 1][j][0] - prices[j], dp[k - 1][i][1])
                    dp[k][i][0] = max(dp[k - 1][j][1] + prices[j], dp[k - 1][i][0])
        print(dp)
        return dp[-1][-1][0]


a = Solution()
# print(a.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# print(a.maxProfit([6, 3, 5, 2, 10, 15]))
# print(a.maxProfit([1, 2, 3, 4, 5]))
# print(a.maxProfit([3, 2, 6, 5, 0, 3]))
print(a.maxProfit([1, 2, 3, 4]))

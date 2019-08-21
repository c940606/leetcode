class Solution:
    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        change_price = []
        n = len(prices)
        for i in range(n - 1):
            change_price.append(prices[i + 1] - prices[i])
        return sum(filter(lambda x: x if x > 0 else 0, change_price))

    def maxProfit1(self, prices):
        if not prices:
            return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        # print("buy:",buy)
        # print("sell:", sell)
        return sell[-1]

    def maxProfit2(self, prices):
        if not prices:
            return 0
        mininum = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < mininum:
                mininum = prices[i]
            elif prices[i] - mininum > 0:
                res += (prices[i] - mininum)
                mininum = prices[i]
        return res

    def maxProfit(self, prices):
        n = len(prices)
        if n == 0: return 0
        dp = [0] * n
        for i in range(1, n):
            for j in range(i + 1):
                dp[i] = max(dp[i], dp[j - 1] + prices[i] - prices[j])
        return dp[-1]


a = Solution()
# print(a.maxProfit1([7,6,4,3,1]))
print(a.maxProfit([7, 1, 5, 3, 6, 4]))

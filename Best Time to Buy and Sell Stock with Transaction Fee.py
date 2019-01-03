class Solution(object):
	def maxProfit(self, prices, fee):
		"""
		:type prices: List[int]
		:type fee: int
		:rtype: int
		"""
		n = len(prices)
		buy = [0] * n
		sell = [0] * n
		buy[0] = -prices[0]
		for i in range(1, n):
			buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
			sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)
			print(buy,"\n",sell)
			print("---")
		return sell[-1]

	def maxProfit1(self, prices, fee):
		mininum = prices[0]
		profit = 0
		for i in range(1, len(prices)):
			if mininum > prices[i]:
				mininum = prices[i]
			elif prices[i] - mininum > fee:
				profit += prices[i] - mininum - fee
				mininum = prices[i] - fee
		return profit
a = Solution()
print(a.maxProfit1(prices = [1, 3, 2, 8, 4, 9], fee = 2))
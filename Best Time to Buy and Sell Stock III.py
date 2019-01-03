class Solution(object):
	def maxProfit(self, prices):
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
			buy1[i] = max(buy1[i-1], -prices[i])
			sell1[i] = max(sell1[i-1],buy1[i-1] + prices[i] )
			buy2[i] = max(buy2[i-1], sell1[i-1] - prices[i])
			sell2[i] = max(sell2[i-1], buy2[i-1] + prices[i])
		return sell2[-1]
a = Solution()
print(a.maxProfit([3,3,5,0,0,3,1,4]))

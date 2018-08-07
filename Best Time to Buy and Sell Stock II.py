class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		change_price = []
		n = len(prices)
		for i in range(n - 1):
			change_price.append(prices[i + 1] - prices[i])
		return sum(filter(lambda x : x if x>0 else 0,change_price))
a = Solution()
print(a.maxProfit([7,6,4,3,1]))
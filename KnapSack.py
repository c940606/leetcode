class Solution:
	def knapSack(self, weights, values, max_weight):
		nums = len(weights)
		dp = [[0] * (max_weight + 1) for _ in range(nums + 1)]
		# print(dp)
		for i in range(1, nums + 1):
			for j in range(max_weight+1):
				if j - weights[i - 1] >= 0:
					dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
				else:
					dp[i][j] = dp[i - 1][j]
		# print(dp)
		return dp[-1][-1]

	def knapSack1(self, weights, values, bag_weight):
		nums = len(weights)
		dp = [0]*(bag_weight+1)
		for i in range(nums):
			for j in range(bag_weight,-1,-1):
				if j >= weights[i]:
					dp[j] = max(dp[j],dp[j-weights[i]]+values[i])
		return dp[-1]



a = Solution()
print(a.knapSack([3, 4, 5], [4, 5, 6], 10))
print(a.knapSack1([3, 4, 5], [4, 5, 6], 10))
print(a.knapSack1([2, 3, 4, 5], [3, 4, 5, 7], 9))

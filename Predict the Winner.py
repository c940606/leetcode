class Solution(object):
	def PredictTheWinner(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		lookup = {}

		def helper(_sum, start, end):
			if (start, end) in lookup:
				return lookup[(start, end)]
			if start == end:
				lookup[(start, end)] = nums[start]
				return nums[start]

			score1 = _sum - helper(_sum - nums[start], start + 1, end)
			print("score1:", score1)
			score2 = _sum - helper(_sum - nums[end], start, end - 1)
			print("score2:", score2)
			res = max(score1, score2)
			print(start, end, res)
			lookup[(start, end)] = res
			return res

		return helper(sum(nums), 0, len(nums) - 1) * 2 >= sum(nums)

	def PredictTheWinner1(self, nums):

		n = len(nums)
		dp = [[0] * n for _ in range(n)]
		for i in range(n):
			dp[i][i] = nums[i]
		for j in range(1, n):
			for k in range(0, n - j):
				s = k + j
				dp[k][s] = max(nums[k] - dp[k + 1][s], nums[s] - dp[k][s - 1])
		print(dp)
		return dp[0][n - 1] >= 0


a = Solution()
print(a.PredictTheWinner1([1, 2, 5]))

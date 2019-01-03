class Solution(object):
	def largestDivisibleSubset(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums: return []
		nums.sort()
		n = len(nums)
		dp = [1] * n
		pre = [-1] * n
		max_count = 0
		max_index = 0
		for i in range(1, n):
			for j in range(0, i):
				if nums[i] % nums[j] == 0:
					# dp[i] = max(dp[j] + 1,dp[i])
					if dp[j] + 1 > dp[i]:
						dp[i] = dp[j] + 1
						pre[i] = j
			if dp[i] > max_count:
				max_count = dp[i]
				max_index = i


		print(dp)
		print(pre)
		print()
		# max_loc = dp.index(max(dp))
		res = []
		while max_index != -1:
			res.append(nums[max_index])
			max_index = pre[max_index]
		return res



a = Solution()
# print(a.largestDivisibleSubset([1, 2, 3]))
# print(a.largestDivisibleSubset([1,2,4,8]))
print(a.largestDivisibleSubset([1]))

class Solution(object):
	def deleteAndEarn(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sum_nums = [0]*10001
		max_nums = 0
		for num in nums:
			sum_nums[num] += 1
			max_nums = max(max_nums,num)
		print(sum_nums,max_nums)
		dp = [0]*(max_nums+1)
		dp[0] = 0
		dp[1] = sum_nums[1]
		print(dp)
		for i in range(2,max_nums+1):
			dp[i] = max(dp[i-1],dp[i-2]+i*sum_nums[i])
		print(dp)
		return dp[-1]
a = Solution()
print(a.deleteAndEarn([2, 2, 3, 3, 3, 4]))
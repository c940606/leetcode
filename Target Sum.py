class Solution(object):
	def findTargetSumWays(self, nums, S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		"""
		if not nums:
			return 0
		n = len(nums)
		self.res = 0

		def helper(idx, S):

			if idx == n:
				if S == 0:
					self.res += 1
				return
			helper(idx + 1, S + nums[idx])
			helper(idx + 1, S - nums[idx])

		helper(0, S)
		return self.res


a = Solution()
print(a.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(a.findTargetSumWays([2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48, 12, 38], 48))

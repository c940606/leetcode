class Solution(object):
	def checkSubarraySum(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		# from collections import defaultdict
		# lookup = defaultdict()
		lookup = {}
		lookup[0] = -1
		# print(lookup)
		summing = 0
		n = len(nums)
		if n < 2 : return False
		for i in range(0,n):
			summing += nums[i]
			summing %= k
			pre = lookup.get(summing,None)
			# print(lookup)
			if pre != None:
				if i - pre > 1:
					return True
			else:
				lookup[summing] = i
		return False


a = Solution()
print(a.checkSubarraySum([23, 2, 4, 6, 7], 6))
print(a.checkSubarraySum([23, 2, 6, 4, 7], 6))
print(a.checkSubarraySum([23, 2, 4, 6, 7], -6))

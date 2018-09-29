class Solution(object):
	def findUnsortedSubarray(self, nums):
		"""
		给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
		你找到的子数组应是最短的，请输出它的长度。
		---
		输入: [2, 6, 4, 8, 10, 9, 15]
		输出: 5
		解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		flag_nums = sorted(nums)
		if flag_nums == nums:
			return 0
		n = len(nums)
		i = 0
		j = n-1
		while i<n and flag_nums[i] == nums[i]:
			i += 1
		while j>-1 and flag_nums[j] == nums[j]:
			j -= 1
		print(i,j)
		return j-i +1
a = Solution()
print(a.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

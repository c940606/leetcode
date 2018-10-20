class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
		你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
		返回滑动窗口最大值。
		---
		输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
		输出: [3,3,5,5,6,7]
		解释:

		  滑动窗口的位置                最大值
		---------------               -----
		[1  3  -1] -3  5  3  6  7       3
		 1 [3  -1  -3] 5  3  6  7       3
		 1  3 [-1  -3  5] 3  6  7       5
		 1  3  -1 [-3  5  3] 6  7       5
		 1  3  -1  -3 [5  3  6] 7       6
		 1  3  -1  -3  5 [3  6  7]      7
		 --
		 思路:

		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		if not nums:return []
		res = []
		cur_max = max(nums[:k])
		res.append(cur_max)
		n = len(nums)
		for i in range(1,n-k+1):
			if nums[i+k-1] > cur_max:
				cur_max = nums[i+k-1]
			elif nums[i-1] == cur_max:
				cur_max = max(nums[i:i+k])
			res.append(cur_max)
		return res
a = Solution()
print(a.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
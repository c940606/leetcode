class Solution(object):
	def search(self, nums, target):
		"""
		给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
		写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
		----
		输入: nums = [-1,0,3,5,9,12], target = 9
		输出: 4
		解释: 9 出现在 nums 中并且下标为 4
		---
		输入: nums = [-1,0,3,5,9,12], target = 2
		输出: -1
		解释: 2 不存在 nums 中因此返回 -1
		---
		思路：
		二分法
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		n = len(nums)
		low = 0
		high = n-1
		while low <= high:
			mid = (low+high)//2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				high = mid - 1
			elif nums[mid] < target:
				low = mid + 1
		return -1
a = Solution()
print(a.search(nums = [-1,0,3,5,9,12], target = 9))

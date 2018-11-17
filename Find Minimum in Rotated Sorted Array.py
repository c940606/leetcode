class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return
		n = len(nums)
		left = 0
		right = n - 1
		while True:
			if nums[left] <= nums[right]:
				return nums[left]
			mid = (left + right) // 2
			print(mid)
			if nums[mid] >= nums[left]:
				left = mid + 1
			else:
				print(mid)
				right = mid
a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))
print(a.findMin([2,1]))
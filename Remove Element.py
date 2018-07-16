class Solution:
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		if nums == []:
			return 0
		while True:
			if val in nums:
				nums.remove(val)
			else:
				break
		return len(nums)
a = Solution()
nums = [3,2,2,3]
val = 3
print(a.removeElement(nums,val))
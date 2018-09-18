class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		print(set(nums))
		if len(set(nums)) == len(nums):
			return False
		return True
a = Solution()
print(a.containsDuplicate([1,2,3,1]))
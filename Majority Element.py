class Solution(object):
	def majorityElement(self, nums):
		"""
		给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
		你可以假设数组是非空的，并且给定的数组总是存在众数
		---

		:type nums: List[int]
		:rtype: int
		"""
		dict = {}
		n = len(nums)
		flg = n//2
		i = 0
		while i < n:
			if nums[i] in dict:
				dict[nums[i]] += 1
				if dict[nums[i]] > flg:
					return nums[i]
			else:
				dict[nums[i]] = 1
			i += 1
		return nums[0]
a = Solution()
print(a.majorityElement([1]))



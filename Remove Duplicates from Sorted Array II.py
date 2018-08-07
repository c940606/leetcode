from collections import Counter


class Solution:
	def removeDuplicates(self, nums):
		"""
		给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
		不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
		:type nums: List[int]
		:rtype: int
		"""
		i = 0
		j = 0
		while True:
			if j>=len(nums)-2:
				return len(nums)
			if nums[i] == nums[j+1]:
				j += 2
				while j<=len(nums)-1 and nums[i] == nums[j]:
					nums.pop(j)
					# j += 1
				i =j
			else:
				i += 1
				j += 1
		return len(nums)
nums = [1,1,1,2,2,3]
nums1 = [0,0,1,1,1,1,2,3,3]
a = Solution()
print(a.removeDuplicates(nums1))

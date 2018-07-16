class Solution:
	def removeDuplicates(self, nums):
		"""
		给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
		不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
		---------
		给定数组 nums = [1,1,2],
		函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
		你不需要考虑数组中超出新长度后面的元素。
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		nums.sort()
		flag = nums[-1]
		i = 0
		while nums[i] != flag:
			while nums[i] == nums[i+1]:
				nums.pop(i+1)
			i += 1
		return i+1
a = Solution()
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [1,23,4,2,1]
print(a.removeDuplicates(nums3))

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

	def removeDuplicates1(self, nums):
		n = len(nums)
		if n < 2:
			return n
		pre = nums[0]
		index = 1
		for i in range(1,n):
			if pre != nums[i]:
				pre = nums[i]
				nums[index] = pre
				index += 1
		return nums

	def removeDuplicates2(self, nums):
		n = len(nums)
		if n < 2:
			return n
		index = 1
		pre = nums[0]
		j = 1
		while True:
			while j < n and pre == nums[j]:
				j += 1
			if j == n:
				break
			pre = nums[j]
			nums[index] = pre
			index += 1
		return nums





a = Solution()
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [1,23,4,2,1]
print(a.removeDuplicates2(nums1))

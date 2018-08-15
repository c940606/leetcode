class Solution(object):
	def majorityElement(self, nums):
		"""
		给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
		说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
		---
		输入: [3,2,3]
		输出: [3]
		---
		:type nums: List[int]
		:rtype: List[int]
		"""
		res = []
		n = len(nums)
		flg = n//3
		tr_nums = set(nums)
		for item in tr_nums:
			if nums.count(item) > flg:
				res.append(item)
		return res
a = Solution()
print(a.majorityElement([1,1,1,3,3,2,2,2]))



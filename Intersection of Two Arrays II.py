class Solution(object):
	def intersect(self, nums1, nums2):
		"""
		给定两个数组，编写一个函数来计算它们的交集。
		---
		输入: nums1 = [1,2,2,1], nums2 = [2,2]
		输出: [2,2]
		---
		输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
		输出: [4,9]
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		res = []
		for item in nums1:
			if item in nums2:
				nums2.remove(item)
				res.append(item)
		return res

	def intersect1(self, nums1, nums2):
		n1 = len(nums1)
		n2 = len(nums2)
		nums1.sort()
		nums2.sort()
		res = []
		i = 0
		j = 0
		while i < n1 and j < n2:
			if nums1[i] == nums2[j]:
				res.append(nums1[i])
				i += 1
				j += 1
			elif nums1[i] > nums2[j]:
				j += 1
			elif nums1[i] < nums2[j]:
				i += 1
		return res
a = Solution()
print(a.intersect1(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))


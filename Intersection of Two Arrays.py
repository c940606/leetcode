class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		给定两个数组，编写一个函数来计算它们的交集。
		----
		输入: nums1 = [1,2,2,1], nums2 = [2,2]
		输出: [2]
		---
		输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
		输出: [9,4]
		---
		思路：

		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		n1 = len(nums1)
		n2 = len(nums2)
		nums1.sort()
		nums2.sort()
		res = []
		i = 0
		j = 0
		while i < n1 and j < n2:
			if i < n1-1 and nums1[i] == nums1[i+1]:
				i += 1
				continue
			if j < n2 - 1 and nums2[j] == nums2[j+1]:
				j += 1
				continue
			if nums1[i] == nums2[j]:
				res.append(nums1[i])
				i += 1
				j += 1
			elif nums1[i] > nums2[j]:
				j += 1
			elif nums1[i] < nums2[j]:
				i += 1
		return (res)
a = Solution()
print(a.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
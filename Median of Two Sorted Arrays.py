class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
		请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
		你可以假设 nums1 和 nums2 不同时为空。
		---
		nums1 = [1, 3]
		nums2 = [2]
		中位数是 2.0
		---
		nums1 = [1, 2]
		nums2 = [3, 4]
		中位数是 (2 + 3)/2 = 2.5
		---
		思路：
		m + n 为奇数 和 偶数
		奇数 找 //2
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		m = len(nums1)
		n = len(nums2)
		if m == 0:
			num = n // 2
			if n % 2 == 0:
				return (nums2[num-1]+nums2[num])/2
			else:
				return nums2[num]
		if n == 0:
			num = m // 2
			if m % 2 == 0:
				return (nums1[num-1]+nums1[num])/2
			else:
				return nums1[num]
		flag = m + n
		# 奇数
		if flag % 2 != 0:
			i = 0
			j = 0
			num = flag //2
			while i < m and j < n and num :
				if nums1[i] < nums2[j]:
					i += 1
				else:
					j += 1
				num -= 1
			if i == m:
				return nums2[j+num]
			if j == n:
				return nums1[i+num]
			if nums1[i] < nums2[j]:
				return nums1[i]
			else:
				return nums2[j]
		else:
			res = []
			i = 0
			j = 0
			num = flag // 2 - 1
			while i < m and j < n and num :
				if nums1[i] < nums2[j]:
					i += 1
				else:
					j += 1
				num -= 1
			print(i,j,num)
			if i == m:
				return (nums2[j+num]+nums2[j+num+1])/2
			if j == n:
				return (i+nums1[num] + nums1[i+num + 1]) / 2
			if nums1[i] < nums2[j]:
				res.append(nums1[i])
				i += 1
			else:
				res.append(nums2[j])
				j += 1
			if i == m:
				return (res[0]+nums2[j])/2
			if j == n:
				return (res[0]+nums1[i])/2
			if nums1[i] < nums2[j]:
				res.append(nums1[i])
			else:
				res.append(nums2[j])
			return sum(res) / 2



a = Solution()
print(a.findMedianSortedArrays(nums1 = [2],nums2 = [1,3,4,5,6]))



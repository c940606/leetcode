class Solution:
	def merge(self, nums1, m, nums2, n):
		"""
		给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
		说明:
		初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
		你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
		----
		输入:
		nums1 = [1,2,3,0,0,0], m = 3
		nums2 = [2,5,6],       n = 3
		输出: [1,2,2,3,5,6]
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		end = m+n-1
		i = m-1
		j = n-1
		while end >= 0 and j >= 0 and i >= 0:
			if nums1[i]<nums2[j]:
				nums1[end] = nums2[j]
				end -= 1
				j -= 1
			else:
				nums1[end] = nums1[i]
				end -= 1
				i -= 1
		if j >= 0:
			nums1[:j+1] = nums2[:j+1]
		return nums1

	def merge1(self, nums1, m, nums2, n):
		i = 0
		j = 0
		base = m
		while j < n and m > 0 and n > 0:
			print(i,j,nums1)
			if nums2[j] <= nums1[i]:
				for s in range(base, i, -1):
					nums1[s] = nums1[s - 1]
				nums1[i] = nums2[j]
				j += 1
		
				base += 1
				print(nums1)
			else:
				i += 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3
		# 输出: [1,2,2,3,5,6]
a = Solution()
print(a.merge1(nums1,m,nums2,n))
# print(a.merge1([0],0,[1],1))
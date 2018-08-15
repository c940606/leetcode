class Solution:
	def findKthLargest(self, nums, k):
		"""
		在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
		---
		思路：
		集合 ---> 排序 --->找到
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		return sorted(nums,reverse=True)[k-1]
nums = [3,2,1,5,6,4]
k = 2
nums1 = [-1,-1]
k1 =2
a = Solution()
print(a.findKthLargest(nums,k))
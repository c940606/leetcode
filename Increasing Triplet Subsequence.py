class Solution(object):
	def increasingTriplet(self, nums):
		"""
		给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
		数学表达式如下:
		如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
		使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
		说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
		---
		输入: [1,2,3,4,5]
		输出: true
		---
		思路1:
		求前i项最小值,后后i项最大值 如果满足递增顺序
		:type nums: List[int]
		:rtype: bool
		"""
		n = len(nums)
		front = [nums[0]]
		for i in range(1,n):
			front.append(min(front[i-1],nums[i]))
		# print(front)
		last = [nums[n-1]]*n
		for i in range(n-2,-1,-1):
			last[i] = max(last[i+1],nums[i])
		# print(last)
		for i in range(n):
			if front[i]<nums[i]<last[i]:
				return True
		return False

	def increasingTriplet1(self, nums):
		a = b = None
		for item in nums:
			if a == None or a>=item:
				a = item
			elif b == None or b>=item:
				b = item
			else:
				return True
		return False


a = Solution()
print(a.increasingTriplet1([5,4,3,2,1]))





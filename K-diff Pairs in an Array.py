class Solution(object):
	def findPairs(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

		if not nums and k < 0:
			return 0
		count = 0
		if k == 0:
			for num in set(nums):
				if nums.count(num) > 1:
					count += 1
			return count
		nums = list(set(nums))
		for num in nums:
			if num + k in nums:
				count += 1
		return count
		# nums.sort()
		# n = len(nums)
		# if n < 2:
		# 	return 0
		#
		# i = 0
		# j = 1
		# # visited = set()
		# # print(nums)
		#
		# while i < n-1 and j < n:
		# 	if nums[j] - nums[i] == k:
		# 		# print(i,j)
		# 		# visited.add((nums[i],nums[j]))
		# 		count += 1
		# 		i += 1
		# 		j = i+1
		# 		continue
		# 	elif nums[j] - nums[i] < k:
		# 		j += 1
		# 		continue
		# 	elif nums[j] - nums[i] > k:
		# 		i += 1
		# 		j = i+1
		# 		continue
		# # print(visited)
		# # return len(visited)
		# return count
a = Solution()
print(a.findPairs([3, 1, 4, 1, 5], k = 2))
print(a.findPairs([1, 2, 3, 4, 5], k = 1))
print(a.findPairs([1, 3, 1, 5, 4], k = 0))
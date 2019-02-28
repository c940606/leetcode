class Solution(object):
	def minSubArrayLen(self, s, nums):
		"""
		给定一个含有 n 个正整数的数组和一个正整数 s ，
		找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
		---
		输入: s = 7, nums = [2,3,1,2,4,3]
		输出: 2
		解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
		---
		思路:
		双指针

		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		n = len(nums)
		i = 0
		j = 0
		min_len = n
		while i < n :
			temp = 0

			j = i
			while j <n and temp < s:
				temp += nums[j]
				j += 1
			if temp >= s and min_len >= (j-i):
				min_len = j-i
				i += 1
			else:
				i += 1
		return 0 if min_len==n else min_len

	def minSubArrayLen1(self, s, nums):
		if not nums:
			return 0
		dp = [0]
		for num in nums:
			dp.append(dp[-1]+num)
		# print(dp)
		n = len(dp)
		res = float("inf")
		for i in range(n-1,-1,-1):
			for j in range(i-1,-1,-1):
				if dp[i] - dp[j] >=s:
					res = min(res,i-j)
					break
		return res if res != float("inf") else 0

	def minSubArrayLen2(self, s, nums):
		cur_sum = 0
		n = len(nums)
		res = float("inf")
		l = 0
		for i in range(n):
			cur_sum += nums[i]
			while cur_sum >= s:
				res = min(res,i-l+1)
				cur_sum -= nums[l]
				l += 1
		return res if res != float("inf") else 0
a = Solution()
print(a.minSubArrayLen2(s = 7, nums = [2,3,1,2,4,3]))
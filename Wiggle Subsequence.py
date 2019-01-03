class Solution:
	def wiggleMaxLength(self, nums):
		"""
		贪心算法
		2,1,4,5,6,3,3,4,8,4

		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n < 2: return n
		res = [nums[0]]
		res_len = 1
		i = 1
		while i < n and nums[i] == nums[i - 1]:
			i += 1
		if i == n: return res_len
		flag = (nums[i] - nums[0]) > 0
		# print("flag:", flag)
		res_len += 1
		res.append(nums[i])
		# print(res,i)
		for i in range(i + 1, n):
			tmp = nums[i] - res[-1]
			if (flag and tmp < 0) or (not flag and tmp > 0):
				res.append(nums[i])
				res_len += 1
				flag = not flag
			elif tmp == 0:
				continue
			else:
				res[-1] = nums[i]
		# print(res)
		return res_len

	def wiggleMaxLength1(self, nums):
		if not nums: return 0
		n = len(nums)
		more_than_0 = [0] * n
		less_than_0 = [0] * n
		more_than_0[0] = 1
		less_than_0[0] = 1
		for i in range(1, n):
			tmp = nums[i] - nums[i - 1]
			if tmp == 0:
				more_than_0[i] = more_than_0[i - 1]
				less_than_0[i] = less_than_0[i - 1]
			elif tmp > 0:
				more_than_0[i] = less_than_0[i-1] + 1
				less_than_0[i] = less_than_0[i-1]
			else:
				less_than_0[i] = more_than_0[i-1] + 1
				more_than_0[i] = more_than_0[i-1]
		return max(less_than_0[-1],more_than_0[-1])


a = Solution()
# print(a.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
# print(a.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
# print(a.wiggleMaxLength([0,0,0]))
print(a.wiggleMaxLength1(
	[33, 53, 12, 64, 50, 41, 45, 21, 97, 35, 47, 92, 39, 0, 93, 55, 40, 46, 69, 42, 6, 95, 51, 68, 72, 9, 32, 84, 34,
	 64, 6, 2, 26, 98, 3, 43, 30, 60, 3, 68, 82, 9, 97, 19, 27, 98, 99, 4, 30, 96, 37, 9, 78, 43, 64, 4, 65, 30, 84, 90,
	 87, 64, 18, 50, 60, 1, 40, 32, 48, 50, 76, 100, 57, 29, 63, 53, 46, 57, 93, 98, 42, 80, 82, 9, 41, 55, 69, 84, 82,
	 79, 30, 79, 18, 97, 67, 23, 52, 38, 74, 15]))

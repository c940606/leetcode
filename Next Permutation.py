class Solution:
	def nextPermutation(self, nums):
		"""
		实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列
		如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
		必须原地修改，只允许使用额外常数空间。
		以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
		1,2,3 → 1,3,2
		3,2,1 → 1,2,3
		1,1,5 → 1,5,1
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		self.nums = int("".join(map(str,nums)))
		sort_nums = sorted(nums)
		if nums == sorted(nums,reverse=True):
			return sort_nums

		self.res = []

		self.trace([],sort_nums)

		return self.res[0]


	def trace(self,temp,sort_nums):
		if sort_nums == [] and self.nums<int("".join(map(str,temp))):

			return self.res.append(temp)
		if sort_nums == []:
			return

		for i in range(len(sort_nums)):
			self.trace(temp+[sort_nums[i]],sort_nums[0:i]+sort_nums[i+1:])

	def nextPermutation1(self, nums):
		'''
		思路:
		 12435 --> 12453
		 有更多的前缀
		:param nums:
		:return:
		'''
		n = len(nums)
		i_flag = 0
		for i in range(n-1,-1,-1):
			if nums[i]>nums[i-1]:
				i_flag = i
				break
		if i_flag != 0:
			for j in range(n-1,i_flag-1,-1):
				if nums[j] > nums[i_flag-1]:
					nums[j],nums[i_flag-1] = nums[i_flag-1],nums[j]
					break
		nums[i_flag:] = nums[i_flag:][::-1]
		return nums
nums = [8,3,5,2]
a = Solution()
print(a.nextPermutation1(nums))

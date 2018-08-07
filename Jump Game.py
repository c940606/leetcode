import sys

class Solution:
	def canJump(self, nums):
		"""
		给定一个非负整数数组，你最初位于数组的第一个位置。
		数组中的每个元素代表你在该位置可以跳跃的最大长度。
		判断你是否能够到达最后一个位置。
		---
		输入: [2,3,1,1,4]
		输出: true
		解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
		:type nums: List[int]
		:rtype: bool
		"""
		#考虑是跳的步数是固定的
# 		n = len(nums)
# 		i = 0
# 		while i < n and nums[i] != 0:
# 			temp = [k+i+1 for k in range(nums[i])]
# 			print(temp)
# 			i = max(map(lambda x:x+nums[x],temp))
# 			print(i)
# 			if i>=n-1:
# 				return True
# 		return False
		self.res = []
		n = len(nums)
		self.flag = 1
		self.Tanxin(0, nums, n, [0])
		print(self.res)
		if len(self.res)>0:
			return True
		else:
			return False


	def Tanxin(self,i,nums,n,temp):
		# if len(self.res)==1:
		# 	sys.exit(0)
		if i >= n-1:
			self.flag = 0
			# print("----")
			self.res.append(temp)
			# sys.exit(0)
			return

		for item in range(i+1,i+nums[i]+1):

			self.Tanxin(item,nums,n,temp+[item])

	def canJump1(self, nums):
		if not nums:
			return True


		i,reach= 0,0
		n = len(nums)
		while i < n-1 and i <= reach:
			reach = max(i+nums[i],reach)
			i += 1
		return reach>=n-1

	def canJump2(self, nums):
		n = len(nums)
		j = n-1
		for i in range(n-2,-1,-1):
			if j - i <= nums[i]:
				j = i
		return j==0

a = Solution()
# [3,2,1,0,4]
# [2,3,1,1,4]
print(a.canJump2([3,2,1,0,4]))

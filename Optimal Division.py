class Solution(object):
	def optimalDivision(self, nums):
		"""
		:type nums: List[int]
		:rtype: str
		"""
		n = len(nums)
		if n == 0:
			return
		if n == 1:
			return nums[0]
		if n == 2:
			return str(nums[0]) + "/" + str(nums[1])
		res = str(nums[0])
		res += "/"
		res += "(" + str(nums[1])
		for i in range(2,n):
			res += "/"+str(nums[i])

		res += ")"
		return res
a = Solution()
print(a.optimalDivision([1000,100,10,2]))
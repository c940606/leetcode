class Solution(object):
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""
		row = len(nums)
		col = len(nums[0])
		size = row * col
		print(size)
		if size != r*c:
			return nums
		flat = []
		for num in nums:
			flat += num
		print(flat)
		res = []
		for i in range(0,size,c):
			print(i)
			res.append(flat[i:i+c])
		return res
a = Solution()
print(a.matrixReshape([[1,2,3,4]],2,2))

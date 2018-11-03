class Solution(object):
	def maxCount(self, m, n, ops):
		"""
		:type m: int
		:type n: int
		:type ops: List[List[int]]
		:rtype: int
		"""
		if not ops:
			return m * n
		# min_num1 = 40001
		# min_num2 = 40001
		res =[]
		for num in zip(*ops):
			# print(num)
			res.append(min(num))
		return min(m * n, res[0]*res[1])
a = Solution()
print(a.maxCount(3,3,[[2,2],[3,3]]))

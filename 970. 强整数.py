class Solution(object):
	def powerfulIntegers(self, x, y, bound):
		"""
		:type x: int
		:type y: int
		:type bound: int
		:rtype: List[int]
		"""
		import math
		res = set()
		if x == 1:
			max_x = 1
		else:
			max_x = int(math.log(bound, x)) + 1
		if y == 1:
			max_y = 1
		else:
			max_y = int(math.log(bound, y)) + 1

		for i in range(max_x):
			for j in range(max_y):
				tmp = x ** i + y ** j
				if tmp <= bound:
					res.add(tmp)
		return list(res)


a = Solution()
print(a.powerfulIntegers(x=2, y=3, bound=10))
print(a.powerfulIntegers(x=3, y=5, bound=15))
print(a.powerfulIntegers(1, 2, 100))
print(a.powerfulIntegers(1, 1, 1))
print(a.powerfulIntegers(1, 1, 2))
print(a.powerfulIntegers(1,1,3))

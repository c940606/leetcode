class Solution(object):
	def bulbSwitch(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		statue = [0] * n
		i = 1
		while i <= n:

			for j in range(i - 1, n, i):
				if statue[j] == 1:
					statue[j] = 0
				else:
					statue[j] = 1
			# print(statue)
			i += 1
		return sum(statue)

	def bulbSwitch1(self, n):
		import math
		return int(math.sqrt(n))


a = Solution()
print(a.bulbSwitch1(9999999))

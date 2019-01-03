class Solution(object):
	def numRabbits(self, answers):
		"""
		:type answers: List[int]
		:rtype: int
		"""
		from collections import defaultdict
		c = defaultdict(int)
		for answer in answers:
			c[answer] += 1
		res = 0
		for key, val in c.items():
			if val % (key + 1) == 0:
				res += (val // (key + 1)) * (key + 1)
			else:
				res += (val // (key + 1) + 1) * (key + 1)

		return res

	def numRabbits1(self, answers):
		from collections import defaultdict
		c = defaultdict(int)
		for answer in answers:
			c[answer] += 1
		return sum([(key + val) // (key + 1) * (key + 1) for key, val in c.items()])


a = Solution()
print(a.numRabbits1([1, 1, 2]))
print(a.numRabbits1([10, 10, 10]))
print(a.numRabbits1([]))

from collections import deque


class Solution(object):
	def minMutation(self, start, end, bank):
		"""
		:type start: str
		:type end: str
		:type bank: List[str]
		:rtype: int
		"""
		if end not in bank:
			return -1
		visited = set()
		def look_cha_one(start):
			for tmp in bank:
				if tmp not in visited and sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(start, tmp))) == 1:
					yield tmp

		stack = deque()
		stack.appendleft([start,0])
		visited.add(start)
		while stack:
			tmp,res = stack.pop()
			if tmp == end:
				return res
			for next in look_cha_one(tmp):
				visited.add(next)
				stack.appendleft((next, res + 1))
		return -1


a = Solution()
print(a.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(a.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(a.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))
print(a.minMutation("AAAAAAAA", "CCCCCCCC",
					["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC",
					 "CCCCCCCA", "CCCCCCCC"]))
print(a.minMutation("AAAACCCC", "CCCCCCCC",
					["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]))

class Solution(object):
	def leastBricks(self, wall):
		"""
		:type wall: List[List[int]]
		:rtype: int
		"""
		from collections import defaultdict
		if not wall:
			return 0
		height = len(wall)
		lookup = defaultdict(int)
		for brick in wall:
			tmp = 0
			for _len in brick[:-1]:
				tmp += _len
				lookup[tmp] += 1

		return height - max(lookup.values()) if lookup else  height


a = Solution()
print(a.leastBricks([[1, 2, 2, 1],
					 [3, 1, 2],
					 [1, 3, 2],
					 [2, 4],
					 [3, 1, 2],
					 [1, 3, 1, 1]]))
print(a.leastBricks([[1],[1],[1]]))

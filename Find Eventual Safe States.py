class Solution(object):
	def eventualSafeNodes(self, graph):
		"""
		:type graph: List[List[int]]
		:rtype: List[int]
		"""
		n = len(graph)
		res = [0] * n

		def helper(i):
			if res[i] == 1: return False
			if res[i] == 2: return True
			res[i] = 1
			for e in graph[i]:
				if not helper(e):
					return False
			res[i] = 2
			return True

		for i in range(n):
			helper(i)
		# print(res)
		return [i for i in range(n) if res[i] == 2]


a = Solution()
print(a.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))

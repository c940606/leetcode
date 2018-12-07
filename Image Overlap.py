class Solution(object):
	def largestOverlap(self, A, B):
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: int
		"""
		from collections import Counter
		row = len(A)
		col = len(A[0])
		lookup = Counter()
		for i in range(row):
			for j in range(col):
				for m in range(row):
					for n in range(col):
						if A[i][j] and B[m][n]:
							lookup[(i - m, j - n)] += 1
		print(lookup.values())
		return max(lookup.values())


a = Solution()
print(a.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))

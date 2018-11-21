class Solution(object):
	def lenLongestFibSubseq(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		lookup = set(A)
		res = 2
		n = len(A)
		for i in range(n):
			for j in range(i + 1, n):
				a = A[i]
				b = A[j]
				temp = 2
				while a + b in lookup:
					a, b, temp = b, a + b, temp + 1
				res = max(res,temp)
		return res


a = Solution()
print(a.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))

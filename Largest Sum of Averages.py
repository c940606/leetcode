class Solution:
	def largestSumOfAverages(self, A, K):
		"""
		:type A: List[int]
		:type K: int
		:rtype: float
		"""
		memo = {}

		def search(n, k):
			if (n, k) in memo:
				return memo[(n, k)]
			if n < k:
				return 0
			if k == 1:
				memo[(n, k)] = sum(A[:n]) / float(n)
				return memo[(n, k)]
			cur, memo[(n, k)] = 0, 0
			for i in range(n - 1, 0, -1):
				cur += A[i]
				memo[(n, k)] = max(memo[(n, k)], search(i, k - 1) + cur / float(n - i))

			return memo[(n, k)]

		return search(len(A), K)


a = Solution()
print(a.largestSumOfAverages(A=[9, 1, 2, 3, 9], K=3))

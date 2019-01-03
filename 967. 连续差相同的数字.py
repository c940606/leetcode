class Solution(object):
	def numsSameConsecDiff(self, N, K):
		"""
		:type N: int
		:type K: int
		:rtype: List[int]
		"""
		res = []

		def helper(tmp, n):
			if n == 0:
				res.append(int(tmp))
				return

			for num in range(0, 10):
				if tmp[0] != "0" and abs(int(tmp[-1]) - num) == K:
					helper(tmp + str(num), n - 1)

		for i in range(0, 10):
			helper(str(i), N - 1)
		return res


a = Solution()
print(a.numsSameConsecDiff(N=3, K=7))
print(a.numsSameConsecDiff(N=2, K=1))
print(a.numsSameConsecDiff(1, 0))

class Solution:
	def checkRecord(self, n: int) -> int:
		import functools, sys
		sys.setrecursionlimit(1000000000)

		M = 10 ** 9 + 7

		@functools.lru_cache(None)
		def dfs(n, A_count, L_count):
			if n == 0:
				return 1
			res = 0
			if A_count == 0:
				res += dfs(n - 1, A_count + 1, 0)
			if L_count < 2:
				res += dfs(n - 1, A_count, L_count + 1)
			res += dfs(n - 1, A_count, 0)
			return res % M

		return dfs(n, 0, 0)

	def checkRecord2(self, n: int) -> int:
		mod = 10 ** 9 + 7
		end_P = [0] * (n + 1)
		end_L = [0] * (n + 1)
		end_P[0] = end_P[1] = end_L[1] = 1
		for i in range(2, n + 1):
			end_P[i] = (end_P[i - 1] + end_L[i - 1]) % mod
			end_L[i] = (end_P[i - 1] + end_P[i - 2]) % mod
		res = (end_P[-1] + end_L[-1]) % mod
		for i in range(n):
			tmp = ((end_P[i] + end_L[i]) % mod + (end_P[n - i - 1] + end_L[n - i - 1]) % mod) % mod
			res += tmp
		return res % mod


a = Solution()
print(a.checkRecord2(100000))

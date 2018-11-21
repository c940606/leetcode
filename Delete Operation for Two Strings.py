class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		n = len(word1)
		m = len(word2)
		if n == 0:
			return m
		if m == 0:
			return n
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(n + 1):
			for j in range(m + 1):
				if i == 0 or j == 0:
					continue
				elif word1[i - 1] == word2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		print(dp[-1][-1])
		max_num = dp[-1][-1]
		return (m+n)- 2*max_num
a = Solution()
print(a.minDistance("sea", "eat"))

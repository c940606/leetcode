class Solution(object):
	def minimumDeleteSum(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: int
		"""
		m = len(s1)
		n = len(s2)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(1, n + 1):
			dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])
		for s in range(1, m + 1):
			dp[s][0] = dp[s - 1][0] + ord(s1[s - 1])
			for k in range(1, n + 1):
				if s1[s - 1] == s2[k - 1]:
					dp[s][k] = dp[s - 1][k - 1]
				else:
					dp[s][k] = min(dp[s][k - 1] + ord(s2[k - 1]), dp[s - 1][k] + ord(s1[s - 1]))
		print(dp)
		return dp[m][n]

	def minimumDeleteSum1(self, s1, s2):
		m = len(s1)
		n = len(s2)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if s1[i - 1] == s2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
				else:
					dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
		print(dp)
		return sum(map(ord,s1+s2)) - dp[m][n]*2


a = Solution()
print(a.minimumDeleteSum(s1="sea", s2="eat"))
print(a.minimumDeleteSum1(s1="sea", s2="eat"))
print(a.minimumDeleteSum(s1="delete", s2="leet"))
print(a.minimumDeleteSum1(s1="delete", s2="leet"))

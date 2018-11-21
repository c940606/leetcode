class Solution(object):
	def longestPalindromeSubseq(self, s):
		"""
		给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
		--
		
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		n = len(s)
		dp = [[0] * n for _ in range(n)]
		for i in range(n - 1, -1, -1):
			dp[i][i] = 1
			for j in range(i + 1, n):
				if s[i] == s[j]:
					dp[i][j] = dp[i + 1][j - 1] + 2
				else:
					dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
		print(dp)
		return dp[0][n-1]


a = Solution()
print(a.longestPalindromeSubseq("bbbab"))
print(a.longestPalindromeSubseq("cbbd"))

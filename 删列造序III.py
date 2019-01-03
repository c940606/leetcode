class Solution(object):
	def minDeletionSize(self, A):
		"""
		:type A: List[str]
		:rtype: int
		"""
		num = len(A)
		word_len = len(A[0])
		dp = [1] * word_len
		for i in range(1, word_len):
			for j in range(i):
				if all(A[k][j] <= A[k][i] for k in range(num)):
					dp[i] = max(dp[i], dp[j] + 1)
		return word_len - max(dp)



a = Solution()
print(a.minDeletionSize(["babca", "bbazb"]))

class Solution(object):
	def findLength(self, A, B):
		"""
		给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
		---
		示例 1:
		输入:
		A: [1,2,3,2,1]
		B: [3,2,1,4,7]
		输出: 3
		解释:
		长度最长的公共子数组是 [3, 2, 1]。
		:type A: List[int]
		:type B: List[int]
		:rtype: int
		"""
		m = len(A)
		n = len(B)
		dp = [[0]*(m+1) for _ in range(n+1)]
		res = 0
		for i in range(1,m+1):
			for j in range(1,n+1):
				# if i == 0 or j == 0:
				# 	continue
				if A[i-1] == B[j-1]:
					dp[i][j]  = 1 + dp[i-1][j-1]
					res = max(res,dp[i][j])
		print(dp)
		return res
a = Solution()
print(a.findLength([1,2,3,2,1],[3,2,1,4,7]))

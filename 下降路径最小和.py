class Solution(object):
	def minFallingPathSum(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		if not A:
			return 0
		row = len(A)
		col = len(A[0])
		self.res = 1000001
		def helper(A,loc,temp_sum):
			if loc == row-1 :
				# print(temp_sum)
				if temp_sum < self.res:
					self.res = temp_sum
				return
			for i in range(col):
				temp = A[loc][i]
				if i == 0:
					helper(A,loc+1,temp_sum+A[loc+1][i]+temp)
					print(temp_sum)
					helper(A, loc + 1, temp_sum + A[loc][i] + A[loc + 1][i+1])

				elif i == col-1:
					helper(A, loc + 1, temp_sum + A[loc][i] + A[loc + 1][i])
					helper(A, loc + 1, temp_sum + A[loc][i] + A[loc + 1][i -1])
				else:
					helper(A, loc + 1, temp_sum + A[loc][i] + A[loc + 1][i - 1])
					helper(A, loc + 1, temp_sum + A[loc][i] + A[loc + 1][i])
					helper(A, loc + 1, temp_sum + A[loc][i] + A[loc + 1][i + 1])


		helper(A,0,0)
		return self.res

	def minFallingPathSum1(self, A):
		if not A:
			return 0
		n = len(A)
		dp = A[::]
		for i in range(1,n):
			for j in range(n):
				if j == 0:
					dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + A[i][j]
				elif j == n-1:
					dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + A[i][j]
				else:
					dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + A[i][j]
		print(dp)
		return min(dp[-1])


a = Solution()
print(a.minFallingPathSum1([[1,2,3],[4,5,6],[7,8,9]]))
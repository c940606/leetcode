class Solution:
    def maxUncrossedLines(self, A, B):
        n1 = len(A)
        n2 = len(B)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


a = Solution()
print(a.maxUncrossedLines(A = [1,4,2], B = [1,2,4]))
print(a.maxUncrossedLines(A = [2,5,1,2,5], B = [10,5,2,1,5,2]))
print(a.maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]))
print(a.maxUncrossedLines([1, 1, 2, 1, 2], [1, 3, 2, 3, 1]))

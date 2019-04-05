class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        A_jia = A[:]
        A_jian = A[:]
        n = len(A)
        for i in range(n):
            A_jia[i] += i
            A_jian[i] -= i
        #print(A_jia)
        #print(A_jian)
        res = float("-inf")
        dp = [None]*n
        dp[-1] = A_jian[-1]
        for i in range(n-2,-1,-1):
            dp[i] = max(dp[i+1],A_jian[i])
        #print(dp)
        for i in range(n-1):
            res = max(A_jia[i]+dp[i+1],res)
        return res

a = Solution()
print(a.maxScoreSightseeingPair([8,1,5,2,6]))
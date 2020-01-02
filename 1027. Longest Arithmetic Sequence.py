from typing import List
class Solution:
    def longestArithSeqLength1(self, A: List[int]) -> int:
        from collections import defaultdict
        n = len(A)
        dp = [defaultdict(lambda:1) for _ in range(n)]
        res = 1
        for i in range(1, n):
            for j in range(i):
                tmp = A[i] - A[j]
                dp[i][tmp] = max(dp[i][tmp], dp[j][tmp] + 1)
                res = max(res, dp[i][tmp])
        return res

    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        n = len(A)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        res = 1
        for i in range(n):
            for j in range(i + 1, n):
                tmp = A[j] - A[i]
                dp[j][tmp] = dp[i][tmp] + 1
                res = max(res, dp[j][tmp])
        return res

a = Solution()
print(a.longestArithSeqLength([83,20,17,43,52,78,68,45]))
print(a.longestArithSeqLength([9,4,7,2,10]))
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        from collections import defaultdict
        if len(A) <= 2: return 0
        dp = [defaultdict(lambda :-1) for _ in range(len(A))]
        res = 0

        for i in range(1, len(A)):
            tmp = A[i] - A[i - 1]
            dp[i][tmp] = dp[i - 1][tmp] + 1
            res += dp[i][tmp]

        print(dp)
        return res


a = Solution()
print(a.numberOfArithmeticSlices([1, 2, 3, 4]))
print(a.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
print(a.numberOfArithmeticSlices([7, 7, 7, 7]))

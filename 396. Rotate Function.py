from typing import List


class Solution(object):
    def maxRotateFunction1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        allSum = 0
        n = len(A)
        F = 0
        for idx, val in enumerate(A):
            F += idx * val
            allSum += val

        res = F
        for i in range(n - 1, 0, -1):
            F = F + allSum - n * A[i]
            res = max(res, F)
        return res

    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        cur = sum(A[i] * i for i in range(n))
        _sum = sum(A)
        res = cur
        for i in range(1, n):
            cur = _sum - n * A[-i] + cur
            res = max(res, cur)
        return res


a = Solution()
print(a.maxRotateFunction(A=[4, 3, 2, 6]))

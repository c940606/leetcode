class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        if not A: return 0
        n = len(A)

        j = 0
        res = 0
        count = 0
        for i in range(n):
            if L <= A[i] <= R:
                res += (i - j + 1)
                count = (i - j + 1)
            elif A[i] < L:
                res += count
            else:
                count = 0
                j = i + 1
        return res


a = Solution()
print(a.numSubarrayBoundedMax([2, 1, 4, 3], 4, 4))
print(a.numSubarrayBoundedMax([16, 69, 88, 85, 79, 87, 37, 33, 39, 34], 55, 57))
print(a.numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8))

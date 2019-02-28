class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        n = len(A)
        if n == 1:
            return 1
        up = 1
        down = 1
        res = 1
        for i in range(0, n - 1):
            if A[i] < A[i + 1]:
                up += 1
                down = 1

            elif A[i] > A[i + 1]:
                down += 1
                up = 1

            else:
                down = 1
                up = 1
            res = max(res, up, down)
            up, down = down, up
        return res


a = Solution()
print(a.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(a.maxTurbulenceSize([4, 8, 12, 16]))

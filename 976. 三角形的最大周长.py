class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        A.sort(reverse=True)
        i = 0

        while i  < n -2:
            if A[i] >= A[i+1] +A[i+2]:
                i += 1
                continue
            else:
                return A[i] + A[i+1] +A[i+2]
        return 0



a = Solution()
print(a.largestPerimeter([3, 6, 2, 3]))
print(a.largestPerimeter([3,2,3,4]))

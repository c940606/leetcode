class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        i = 0
        j = n-1
        res = [0]*n
        for s in range(n-1,-1,-1):
            if abs(A[i]) > abs(A[j]):
                res[s] = A[i] * A[i]
                i += 1
            else:
                res[s] = A[j] * A[j]
                j -= 1
        return  res
a = Solution()
print(a.sortedSquares([-4,-1,0,3,10]))
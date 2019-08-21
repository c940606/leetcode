class Solution:
    def prevPermOpt1(self, A):
        n = len(A)
        left = n - 2
        right = n - 1
        while left >= 0 and A[left] <= A[left + 1]:
            left -= 1
        if left < 0: return A
        while right >=0 and A[left] <= A[right]:
            right -= 1
        while right >0 and A[right] == A[right-1]:
            right -= 1
        A[left], A[right] = A[right], A[left]
        return A
a = Solution()
print(a.prevPermOpt1([1,9,4,6,7]))
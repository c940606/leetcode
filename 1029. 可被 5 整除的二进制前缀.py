class Solution:
    def prefixesDivBy5(self, A):
        for idx, val in enumerate(A[1:], 1):
            A[idx] += A[idx-1] * 2 % 5
        #print(A)
        return [a % 5 == 0 for a in A]


a = Solution()
print(a.prefixesDivBy5([0, 1, 1]))
print(a.prefixesDivBy5([1, 1, 1]))
print(a.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
print(a.prefixesDivBy5([0, 1, 1]))

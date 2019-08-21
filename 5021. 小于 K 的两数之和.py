class Solution:
    def twoSumLessThanK(self, A, K) -> int:
        A.sort()
        n = len(A)
        left = 0
        right = n - 1
        res = -1
        while left < right:
            tmp = A[right] + A[left]
            if tmp < K:
                if K - res > K - tmp:
                    res = tmp
                left += 1
            else:
                right -= 1
        return res


a = Solution()
print(a.twoSumLessThanK(A=[34, 23, 1, 24, 75, 33, 54, 8], K=60))
print(a.twoSumLessThanK(A=[10, 20, 30], K=15))
print(a.twoSumLessThanK([1], 1))
print(a.twoSumLessThanK(
    [254, 914, 110, 900, 147, 441, 209, 122, 571, 942, 136, 350, 160, 127, 178, 839, 201, 386, 462, 45, 735, 467, 153,
     415, 875, 282, 204, 534, 639, 994, 284, 320, 865, 468, 1, 838, 275, 370, 295, 574, 309, 268, 415, 385, 786, 62,
     359, 78, 854, 944], 200))

class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:

        M = 10 ** 9 + 7
        _sum = sum(arr)
        prev = 0
        cur_num = 0
        res = 0
        for a in arr * 2:
            cur_num += a
            res = max(res, cur_num - prev)
            prev = min(cur_num, prev)
        if _sum <= 0:
            return res % M
        else:
            res += (k - 2) * _sum
            return res % M


a = Solution()
print(a.kConcatenationMaxSum([1, 3], 1))
print(a.kConcatenationMaxSum([1, 2], 3))
print(a.kConcatenationMaxSum([1, -2, 1], 5))
print(a.kConcatenationMaxSum([-1, -2], 7))
print(a.kConcatenationMaxSum([-1, 1, 3, -2, 2, -3], 3))
print(a.kConcatenationMaxSum([-5, -2, 0, 0, 3, 9, -2, -5, 4], 5))

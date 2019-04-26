class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        if n <= 2:
            return 2
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                tmp = 2
                c = A[j] - A[i]
                next_num = A[j] + c
                t = j
                while True:
                    if next_num in A:
                        loc = A.rindex(next_num)
                        if loc > t:
                            tmp += 1
                            next_num += c
                            t = loc
                        else:
                            break
                    else:
                        break
                res = max(res, tmp)
        return res

    def longestArithSeqLength1(self, A):
        from collections import defaultdict
        dp = defaultdict(lambda: 1)
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                dp[b - a, j] = max(dp[b - a, j], dp[b - a, i] + 1)
        return max(dp.values())

    def longestArithSeqLength2(self, A):
        from collections import defaultdict
        dp = defaultdict(lambda: 1)
        n = len(A)
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                dp[d, i] = max(dp[d, j] + 1, dp[d, i])
        return max(dp.values())


a = Solution()
# print(a.longestArithSeqLength([9,4,7,2,10]))
# print(a.longestArithSeqLength([20,1,15,3,10,5,8]))
# print(a.longestArithSeqLength([3,6,9,12]))
print(a.longestArithSeqLength2(
    [44, 46, 22, 68, 45, 66, 43, 9, 37, 30, 50, 67, 32, 47, 44, 11, 15, 4, 11, 6, 20, 64, 54, 54, 61, 63, 23, 43, 3, 12,
     51, 61, 16, 57, 14, 12, 55, 17, 18, 25, 19, 28, 45, 56, 29, 39, 52, 8, 1, 21, 17, 21, 23, 70, 51, 61, 21, 52, 25,
     28]))

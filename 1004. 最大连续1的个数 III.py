class Solution:
    def longestOnes(self, A, K):
        dp = [0]
        for a in A:
            dp.append(dp[-1] + a)

        n = len(A)
        print(dp, n)
        res = 0
        for i in range(n, -1, -1):
            for j in range(0, i):
                # print(dp[i],dp[j])
                if dp[i] - dp[j] == K + 1:
                    res = max(i - j + 1, res)

        return res

    def longestOnes1(self, A, K):
        left = 0
        res = 0
        for idx, val in enumerate(A):
            if val == 0:
                K -= 1
            while K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            res = max(res, idx - left + 1)
        return res


a = Solution()
print(a.longestOnes1(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
print(a.longestOnes1(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))

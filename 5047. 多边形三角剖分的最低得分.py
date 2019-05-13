class Solution:
    def minScoreTriangulation(self, A):
        """

        :param A:
        :return:
        """
        n = len(A)
        if n < 3: return

        def cheng(tmp):
            res = 1
            for t in tmp:
                res *= t
            return res

        if n == 3:
            return cheng(A)

        def helper(c_A, n, i):
            ans = 0
            count = n // 2
            sheng = n - 2 - count
            j = i
            while count:
                ans += cheng(c_A[i:i + 3])
                i += 2
                count -= 1
            print(ans)
            while sheng:
                ans += c_A[j] * c_A[j + 2] * c_A[j + 4]
                j += 4
                sheng -= 1
            return ans

        c_A = A * 2
        print(helper(c_A, n, 1))

        # return min(helper(c_A, n, 0), helper(c_A, n, 1), helper(c_A, n, 2))

    def minScoreTriangulation1(self, A):
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n):
            for i in range(n):
                if i + d < n:
                    j = i + d
                    dp[i][j] = float("inf")
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        return dp[0][-1]


a = Solution()
print(a.minScoreTriangulation1([3, 7, 4, 5]))
print(a.minScoreTriangulation1([1, 3, 1, 4, 1, 5]))
print(a.minScoreTriangulation1([2, 2, 2, 2, 1]))
print(a.minScoreTriangulation1([3, 1, 4, 5, 4]))

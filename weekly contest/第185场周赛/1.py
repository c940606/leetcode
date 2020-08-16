class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[0] * (100 + 1) for _ in range(100 + 1)]
        num = [0] * (100 + 1)
        for i in range(1, 100 + 1):
            num[i] = i
            dp[i][1] = 1

        for i in range(2, 100 + 1):
            for j in range(1, 100 + 1):
                for s in range(i - 1, 0, -1):
                    if num[i] > num[s] and num[i] < m:
                        dp[i][j] += dp[s][j - 1]
        res = 0
        for i in range(1, n + 1):
            res += dp[i][k]
        return res

a  = Solution()
print(a.numOfArrays(n = 2, m = 3, k = 1))

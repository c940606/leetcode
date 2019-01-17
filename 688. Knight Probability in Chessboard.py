class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp0 = [[1] * N for _ in range(N)]
        steps = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        print(dp0)
        for c in range(K):
            dp1 = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for x, y in steps:
                        row = i + x
                        col = j + y
                        if 0 <= row < N and 0 <= col < N:
                            dp1[i][j] += dp0[row][col]
            dp0 = dp1
        return dp0[r][c] / (8 ** K)


a = Solution()
print(a.knightProbability(3, 2, 0, 0))

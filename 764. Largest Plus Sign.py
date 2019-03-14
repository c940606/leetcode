class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N] * N for _ in range(N)]

        for mine in mines:
            grid[mine[0]][mine[1]] = 0
        # print(grid)

        for i in range(N):
            left = 0
            right = 0
            up = 0
            down = 0
            for j, s in zip(range(N), reversed(range(N))):
                # left
                left = left + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], left)

                # right
                right = right + 1 if grid[i][s] != 0 else 0
                grid[i][s] = min(grid[i][s], right)

                # up
                up = up + 1 if grid[j][i] != 0 else 0
                grid[j][i] = min(grid[j][i], up)

                # down
                down = down + 1 if grid[s][i] != 0 else 0
                grid[s][i] = min(grid[s][i], down)
        # print(grid)
        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, grid[i][j])
        return res

    def orderOfLargestPlusSign1(self, N, mines):

        dp = [[N] * N for _ in range(N)]

        for x, y in mines:
            dp[x][y] = 0

        # print(dp)
        for i in range(N):
            left = 0
            right = 0
            up = 0
            down = 0
            for j, k in zip(range(N), range(N - 1, -1, -1)):
                left = left + 1 if dp[i][j] != 0 else 0
                right = right + 1 if dp[i][k] != 0 else 0
                up = up + 1 if dp[j][i] != 0 else 0
                down = down + 1 if dp[k][i] != 0 else 0

                dp[i][j] = min(dp[i][j], left)
                dp[i][k] = min(dp[i][k], right)
                dp[j][i] = min(dp[j][i], up)
                dp[k][i] = min(dp[k][i], down)

        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, dp[i][j])
        return res


a = Solution()
print(a.orderOfLargestPlusSign1(N=5, mines=[[4, 2]]))
print(a.orderOfLargestPlusSign1(5,
                                [[0, 0], [0, 1], [0, 4], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                                 [3, 0], [4, 0], [4, 1], [4, 3], [4, 4]]))
# print(a.orderOfLargestPlusSign1(1000, []))
print(a.orderOfLargestPlusSign(5,
                               [[0, 0], [0, 1], [0, 4], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                                [3, 0], [4, 0], [4, 1], [4, 3], [4, 4]]))

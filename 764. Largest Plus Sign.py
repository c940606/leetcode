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


a = Solution()
# print(a.orderOfLargestPlusSign(N=5, mines=[[4, 2]]))
print(a.orderOfLargestPlusSign(5,
                               [[0, 0], [0, 1], [0, 4], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                                [3, 0], [4, 0], [4, 1], [4, 3], [4, 4]]))
print(a.orderOfLargestPlusSign(1000,[]))

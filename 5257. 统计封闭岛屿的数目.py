from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0
        self.flag = True

        def dfs(i, j):
            grid[i][j] = 1
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                self.flag = False
                return
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0:
                    dfs(tmp_i, tmp_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dfs(i, j)
                    if self.flag:
                        cnt += 1
                self.flag = True
        return cnt


a = Solution()
print(a.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
print(a.closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(a.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                           [1, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1, 1, 1]]))

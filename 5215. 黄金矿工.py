class Solution:
    def getMaximumGold(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        self.res = 0

        def dfs(i, j, tmp, visited):
            visited.add((i, j))
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] != 0 and \
                        (tmp_i, tmp_j) not in visited:
                    dfs(tmp_i, tmp_j, tmp + grid[tmp_i][tmp_j], visited)
            visited.remove((i, j))
            self.res = max(self.res, tmp)

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    dfs(i, j, grid[i][j], set())
        return self.res


a = Solution()
print(a.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
print(a.getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))

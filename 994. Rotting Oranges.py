from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        dict = {}

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dict[(i, j)] = float("inf")

        if not dict:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def Is(x, y):
            return x >= 0 and x < row and y >= 0 and y < col

        def dfs(x, y, dis):
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if Is(new_x, new_y) and (new_x, new_y) not in visited and grid[new_x][new_y] == 1:
                    visited.add((new_x, new_y))
                    dict[(new_x, new_y)] = min(dict[(new_x, new_y)], dis + 1)
                    print(new_x, new_y, dis)
                    dfs(new_x, new_y, dis + 1)
                    visited.remove((new_x, new_y))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    visited = set()
                    dfs(i, j, 0)
        return max(dict.values()) if max(dict.values()) < float("inf") else -1


a = Solution()
print(a.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(a.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))

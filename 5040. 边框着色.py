class Solution:
    def colorBorder(self, grid, r0, c0, color):
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])
        boarder = []

        def dfs(r, c):

            for x, y in dirs:
                tmp_r = r + x
                tmp_c = c + y
                if 0 <= tmp_r < row and 0 <= tmp_c < col and grid[tmp_r][tmp_c] == grid[r][c]:
                    if (tmp_r, tmp_c) not in visited:
                        visited.add((tmp_r, tmp_c))
                        dfs(tmp_r, tmp_c)
                else:
                    boarder.append([r, c])

        dfs(r0, c0)
        for x, y in boarder:
            grid[x][y] = color
        return grid

    def colorBorder1(self, grid, r0, c0, color):
        from collections import deque
        visited = set()
        boarder = []
        queue = deque()
        queue.appendleft((r0, c0))
        visited.add((r0, c0))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(grid)
        col = len(grid[0])
        #print(queue)
        while queue:
            x, y = queue.pop()
            for i, j in dirs:
                tmp_x = i + x
                tmp_y = j + y
                if 0 <= tmp_x < row and 0 <= tmp_y < col and grid[tmp_x][tmp_y] == grid[x][y]:
                    if (tmp_x, tmp_y) not in visited:
                        visited.add((tmp_x, tmp_y))
                        queue.appendleft((tmp_x, tmp_y))
                else:
                    boarder.append([x, y])
        for x, y in boarder:
            grid[x][y] = color
        return grid


a = Solution()
print(a.colorBorder1(grid=[[1, 1], [1, 2]], r0=0, c0=0, color=3))
# print(a.colorBorder(grid=[[1, 2, 2], [2, 3, 2]], r0=0, c0=1, color=3))
# print(a.colorBorder(grid=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], r0=1, c0=1, color=2))

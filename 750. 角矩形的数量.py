class Solution:
    def countCornerRectangles1(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                # 左上角
                if grid[i][j] == 0:
                    continue

                for s in range(i + 1, row):
                    if grid[s][j] == 0:
                        continue
                    for k in range(j + 1, col):
                        if grid[i][k] == 1 and grid[s][k] == 1:
                            res += 1
        return res

    def countCornerRectangles2(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(i + 1, row):
                tmp = 0
                for k in range(col):
                    if grid[i][k] == 1 and grid[j] == 1:
                        tmp += 1
                res += tmp * (tmp - 1) / 2
        return res

    def countCornerRectangles(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row - 1):
            one = []
            for k in range(col):
                if grid[i][k] == 1:
                    one.append(k)
            for j in range(i+1, row):
                tmp = 0
                for t in one:
                    if grid[j][t] == 1:
                        tmp += 1
                res += tmp * (tmp - 1) // 2
        return res

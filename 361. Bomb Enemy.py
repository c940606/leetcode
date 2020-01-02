from typing import List


class Solution:
    def maxKilledEnemies1(self, grid):

        res = float("-inf")
        row = len(grid)
        col = len(grid[0])

        def helper(i, j):
            # 行
            ans = 0
            left = j - 1
            right = j + 1
            while left >= 0 and grid[i][left] != "W":
                if grid[i][left] == "E":
                    ans += 1
                left -= 1
            while right < col and grid[i][right] != "W":
                if grid[i][right] == "E":
                    ans += 1
                right += 1
            # 列
            up = i - 1
            down = i + 1
            while up >= 0 and grid[up][j] != "W":
                if grid[up][j] == "E":
                    ans += 1
                up -= 1
            while down < row and grid[down][j] != "W":
                if grid[down][j] == "E":
                    ans += 1
                down += 1
            return ans

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    tmp = helper(i, j)
                    print(tmp)
                    res = max(tmp, res)

        return res

    def maxKilledEnemies2(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        r = len(grid)
        c = len(grid[0])

        def cal(row, col):
            res = 0
            left, right = col - 1, col + 1
            while left >= 0 and grid[row][left] != "W":
                if grid[row][left] == "E":
                    res += 1
                left -= 1
            while right < c and grid[row][right] != "W":
                if grid[row][right] == "E":
                    res += 1
                right += 1
            up, down = row - 1, row + 1
            while up >= 0 and grid[up][col] != "W":
                if grid[up][col] == "E":
                    res += 1
                up -= 1
            while down < r and grid[down][col] != "W":
                if grid[down][col] == "E":
                    res += 1
                down += 1
            return res

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "0":
                    res = max(res, cal(i, j))
        return res

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]
        res = 0
        for i in range(row):
            tmp1 = [0] * col
            tmp1[0] = 1 if grid[i][0] == "E" else 0
            # left to right
            for j in range(1, col):
                if grid[i][j] == "E":
                    tmp1[j] = tmp1[j - 1] + 1
                elif grid[i][j] == "W":
                    continue
                else:
                    tmp1[j] = tmp1[j - 1]
            tmp2 = [0] * col
            tmp2[-1] = 1 if grid[i][-1] == "E" else 0
            # right to left
            for k in range(col - 2, -1, -1):
                if grid[i][k] == "E":
                    tmp2[k] = tmp2[k + 1] + 1
                elif grid[i][k] == "W":
                    continue
                else:
                    tmp2[k] = tmp2[k + 1]
            # 求总和
            for t in range(col):
                if grid[i][t] == "0":
                    dp[i][t] = tmp1[t] + tmp2[t]

        # print(dp)
        for i in range(col):
            tmp1 = [0] * row
            tmp1[0] = 1 if grid[0][i] == "E" else 0
            # up to down
            for j in range(1, row):
                if grid[j][i] == "E":
                    tmp1[j] = tmp1[j - 1] + 1
                elif grid[j][i] == "W":
                    continue
                else:
                    tmp1[j] = tmp1[j - 1]
            tmp2 = [0] * row
            tmp2[-1] = 1 if grid[-1][i] == "E" else 0
            # down to up
            for k in range(row - 2, -1, -1):
                if grid[k][i] == "E":
                    tmp2[k] = tmp2[k + 1] + 1
                elif grid[k][i] == "W":
                    continue
                else:
                    tmp2[k] = tmp2[k + 1]
            # 求总和
            for t in range(row):
                if grid[t][i] == "0":
                    dp[t][i] += tmp1[t] + tmp2[t]
                    res = max(dp[t][i], res)
        return res


a = Solution()
print(a.maxKilledEnemies([["0", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "W"]]))
print(a.maxKilledEnemies([["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]))

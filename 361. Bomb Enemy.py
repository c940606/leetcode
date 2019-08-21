class Solution:
    def maxKilledEnemies(self, grid):

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


a = Solution()
print(a.maxKilledEnemies([["0","E","E","E","E","E","E","E","E","E","E","W"]]))
# print(a.maxKilledEnemies([["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]))

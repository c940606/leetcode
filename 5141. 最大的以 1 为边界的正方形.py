class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        max_e = min(row, col)

        def helper(i, j, max_e):
            for x in range(i, i+max_e ):
                if grid[x][j] == 0 or grid[x][j+max_e-1] == 0:
                    return False
            for y in range(j, j + max_e):
                if grid[i][y] == 0 or grid[i+max_e-1][y] == 0:
                    return False

            return True

        while max_e:
            for i in range(0, row - max_e + 1):
                for j in range(0, col - max_e + 1):
                    if helper(i,j,max_e):
                        return max_e * max_e

            max_e -= 1
        return 0

a = Solution()
print(a.largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]))
print(a.largest1BorderedSquare(grid = [[1,1,0,0]]))

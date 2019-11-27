class Solution:
    def shiftGrid(self, grid, k: int):
        row = len(grid)
        col = len(grid[0])
        tmp = sum(grid, [])
        # print(tmp)
        k %= len(tmp)
        tmp = tmp[-k:] + tmp[:-k]
        # print(tmp)
        res = []
        for i in range(0, len(tmp), col):
            res.append(tmp[i:i + col])
        return res


a = Solution()
print(a.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
print(a.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
print(a.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=10))

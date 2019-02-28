class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # print(grid)
        row = len(grid)
        col = len(grid[0])
        vistied = set()
        access_grid = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == -1:
                    vistied.add((i, j))
                else:
                    access_grid += 1
        # print(vistied)
        self.res = 0

        def helper(i, j, num):
            if (i, j) == end and num == access_grid - 1:
                self.res += 1
                return
            vistied.add((i, j))
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i, tmp_j = i + x, j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in vistied:
                    helper(tmp_i, tmp_j, num + 1)
            vistied.remove((i, j))

        helper(*start, 0)
        return self.res


a = Solution()
print(a.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print(a.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
print(a.uniquePathsIII([[0, 1], [2, 0]]))

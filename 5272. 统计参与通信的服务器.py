from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        row = defaultdict(set)
        col = defaultdict(set)
        res = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[i].add((i, j))
                    col[j].add((i, j))
        for r, v in row.items():
            if len(v) > 1:
                res.update(v)
        for c, v in col.items():
            if len(v) > 1:
                res.update(v)
        return len(res)


a = Solution()
print(a.countServers(grid=[[1, 0], [0, 1]]))

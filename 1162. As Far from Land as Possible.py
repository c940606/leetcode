from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        step = -1
        seas = set()
        n = len(grid)
        m = len(grid[0])
        flag = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    seas.add((i, j))
                else:
                    flag += 1
        print(seas)
        while seas and flag:
            # print(seas)
            step += 1
            nxt_seas = set()
            for i, j in seas:
                for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    tmp_i = i + x
                    tmp_j = j + y
                    # if grid[tmp_i][tmp_j] == 1: return step
                    if 0 <= tmp_i < n and 0 <= tmp_j < m and grid[tmp_i][tmp_j] == 0:
                        grid[tmp_i][tmp_j] = 1
                        nxt_seas.add((tmp_i, tmp_j))
            seas = nxt_seas
        return step


a = Solution()
# print(a.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
# print(a.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
print(a.maxDistance([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))

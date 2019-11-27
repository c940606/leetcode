from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        row = len(grid)
        col = len(grid[0])
        distance = [[0] * col for _ in range(row)]
        cnt = [[-1] * col for _ in range(row)]
        # print(distance)
        homes = set()
        zero_loc = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    homes.add((i, j))
                elif grid[i][j] == 0:
                    cnt[i][j] = 0
                    zero_loc += 1

        def bfs(i, j):
            step = 0
            queue = deque([(i, j)])
            visited = set([(i, j)])
            while queue:
                n = len(queue)
                for _ in range(n):
                    i, j = queue.pop()
                    cnt[i][j] += 1
                    distance[i][j] += step
                    for x, y in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 0 \
                                and (tmp_i, tmp_j) not in visited:
                            visited.add((tmp_i, tmp_j))
                            queue.appendleft((tmp_i, tmp_j))
                step += 1

        if not zero_loc: return -1
        for i, j in homes:
            bfs(i, j)
        return min([distance[i][j] for i in range(row) for j in range(col) if cnt[i][j] == len(homes)] or [-1])


a = Solution()
print(a.shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(a.shortestDistance([[1, 0]]))
print(a.shortestDistance([[1, 1], [0, 1]]))

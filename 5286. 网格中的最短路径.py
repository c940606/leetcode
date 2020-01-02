from collections import deque

class Solution:
    def shortestPath(self, grid, k: int) -> int:
        from collections import deque
        queue = deque([(0, 0, k, 0)])
        row  = len(grid)
        col = len(grid[0])
        visited = set([(0, 0, k)])
        while queue:

            n = len(queue)
            for _ in range(n):
                i, j, k, step = queue.pop()
                if i == row - 1 and j == col - 1:
                    return step
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    tmp_i = x + i
                    tmp_j = y + j
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j, k) not in visited:
                        visited.add((tmp_i, tmp_j, k))
                        if grid[tmp_i][tmp_j] == 0:
                            queue.appendleft((tmp_i, tmp_j, k, step + 1))
                        if grid[tmp_i][tmp_j] == 1 and k >= 1:
                            queue.appendleft((tmp_i, tmp_j, k - 1, step + 1))
        return -1

a = Solution()
print(a.shortestPath(grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1))
print(a.shortestPath(grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1))
# print(a.shortestPath([[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1],[0,0,0,1,0,0,1,0]],
# 1))
# print(a.shortestPath([[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]]
# ,27))
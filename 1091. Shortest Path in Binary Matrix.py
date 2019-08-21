class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        from collections import deque
        queue = deque()
        N = len(grid)
        visited = set()
        if grid[0][0] == 0:
            queue.appendleft((0, 0, 1))
        visited.add((0, 0))
        while queue:
            i, j, res = queue.pop()
            if i == N - 1 and j == N - 1:
                return res
            for x, y in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < N and 0 <= tmp_j < N and grid[tmp_i][tmp_j] == 0 and (tmp_i, tmp_j) not in visited:
                    visited.add((tmp_i, tmp_j))
                    queue.appendleft((tmp_i, tmp_j, res + 1))
        return -1


a = Solution()
print(a.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
print(a.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))

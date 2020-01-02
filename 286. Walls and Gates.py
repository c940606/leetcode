from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def dfs(i, j, steps):
            if i < 0 or i >= row or j < 0 or j >= col or rooms[i][j] < steps:
                return
            rooms[i][j] = min(rooms[i][j], steps)
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                dfs(x + i, y + j, steps + 1)

        def bfs(i, j):
            from collections import deque

            queue = deque([[i, j, 0]])
            while queue:
                n = len(queue)
                for _ in range(n):
                    i, j, step = queue.pop()
                    rooms[i][j] = step
                    for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        if 0 <= i + x < row and 0 <= j + y < col and rooms[i + x][j + y] > step + 1:
                            queue.append([i + x, j + y, step + 1])

        row = len(rooms)
        col = len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
                    # bfs(i, j)
        print(rooms)


a = Solution()
# print(a.wallsAndGates([[2147483647, 2147483647, 0]]))
# print(a.wallsAndGates(
#     [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
#      [0, -1, 2147483647, 2147483647]]))
print(a.wallsAndGates([[0, 2147483647, -1, 2147483647, 2147483647, -1, -1, 0, 0, -1, 2147483647, 2147483647, 0, -1,
                        2147483647, 2147483647, 2147483647, 2147483647, 0, 2147483647, 0, -1, -1, -1, -1, 2147483647,
                        -1, -1, 2147483647, 2147483647, -1, -1, 0, 0, -1, 0, 0, 0, 2147483647, 0, 2147483647, -1, -1, 0,
                        -1, 0, 0, 0, 2147483647],
                       [2147483647, 0, -1, 2147483647, 0, -1, -1, -1, -1, 0, 0, 2147483647, 2147483647, -1, -1,
                        2147483647, -1, -1, 2147483647, 2147483647, -1, 0, -1, 2147483647, 0, 2147483647, -1,
                        2147483647, 0, 2147483647, 0, 2147483647, -1, 2147483647, 0, 2147483647, -1, 2147483647, 0,
                        2147483647, 2147483647, 0, -1, 2147483647, -1, -1, -1, 0, 2147483647]]))

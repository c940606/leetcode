class Solution:
    def minimumMoves(self, grid) -> int:
        from collections import deque
        n = len(grid)
        if grid[0][0] == 1 or grid[0][1] or grid[n - 1][n - 2] or grid[n - 1][n - 1]:
            return -1
        target = (n - 1, n - 2, n - 1, n - 1)
        # print(target)
        bfs = deque()
        bfs.appendleft((0, 0, 0, 1))
        step = 0
        visited = set()
        visited.add((0, 0, 0, 1))

        while bfs:
            c = len(bfs)
            # print(bfs)
            for _ in range(c):
                x1, y1, x2, y2 = bfs.pop()
                # print(x1, y1, x2, y2)
                if (x1, y1, x2, y2) == target:
                    return step
                # 水平
                if x1 == x2:
                    # right
                    if y2 + 1 < n and grid[x1][y2 + 1] != 1 and (x2, y2, x2, y2 + 1) not in visited:
                        tmp = (x2, y2, x2, y2 + 1)
                        bfs.appendleft(tmp)
                        visited.add(tmp)
                    # down
                    if x1 + 1 < n and grid[x1 + 1][y1] != 1 and grid[x1 + 1][y2] != 1 and (
                            x1 + 1, y1, x1 + 1, y2) not in visited:
                        tmp = (x1 + 1, y1, x1 + 1, y2)
                        bfs.appendleft(tmp)
                        visited.add(tmp)
                    # 顺时针
                    if x1 + 1 < n and grid[x1 + 1][y1] != 1 and grid[x1 + 1][y2] != 1 and \
                            (x1, y1, x1 + 1, y1) not in visited:
                        tmp = (x1, y1, x1 + 1, y1)
                        bfs.appendleft(tmp)
                        visited.add(tmp)
                # 垂直
                if y1 == y2:
                    # right
                    if y1 + 1 < n and grid[x1][y1 + 1] != 1 and grid[x2][y1 + 1] != 1 and (
                            x1, y1 + 1, x2, y1 + 1) not in visited:
                        tmp = (x1, y1 + 1, x2, y1 + 1)
                        visited.add(tmp)
                        bfs.appendleft(tmp)
                    # down
                    if x2 + 1 < n and grid[x2 + 1][y1] != 1 and (x2, y2, x2 + 1, y2) not in visited:
                        tmp = (x2, y2, x2 + 1, y2)
                        visited.add(tmp)
                        bfs.appendleft(tmp)
                    # 逆时针
                    if y1 + 1 < n and grid[x1][y1 + 1] != 1 and grid[x2][y2 + 1] != 1 and (
                    x1, y1, x1, y1 + 1) not in visited:
                        tmp = (x1, y1, x1, y1 + 1)
                        visited.add(tmp)
                        bfs.appendleft(tmp)
            step += 1
        return -1


a = Solution()
print(a.minimumMoves(grid=[[0, 0, 0, 0, 0, 1],
                           [1, 1, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1, 1],
                           [0, 0, 1, 0, 1, 0],
                           [0, 1, 1, 0, 0, 0],
                           [0, 1, 1, 0, 0, 0]]))
print(a.minimumMoves([[0, 0, 1, 1, 1, 1],
                      [0, 0, 0, 0, 1, 1],
                      [1, 1, 0, 0, 0, 1],
                      [1, 1, 1, 0, 0, 1],
                      [1, 1, 1, 0, 0, 1],
                      [1, 1, 1, 0, 0, 0]]))

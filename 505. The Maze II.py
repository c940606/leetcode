from typing import List


class Solution:
    def shortestDistance1(self, maze, start, destination):
        from collections import defaultdict
        row = len(maze)
        col = len(maze[0])

        lookup = defaultdict(lambda: float("inf"))
        lookup[(start[0], start[1])] = 0

        def dfs(i, j):
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                res = 0
                tmp_i = i
                tmp_j = j
                while 0 <= tmp_i + x < row and 0 <= tmp_j + y < col \
                        and maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                    res += 1
                # print(tmp_i,tmp_j)
                if tmp_i == i and tmp_j == j: continue
                # if (tmp_i, tmp_j) not in visited:
                if lookup[(i, j)] + res < lookup[(tmp_i, tmp_j)]:
                    lookup[(tmp_i, tmp_j)] = lookup[(i, j)] + res
                    dfs(tmp_i, tmp_j)

        dfs(start[0], start[1])
        return lookup[(destination[0], destination[1])] if lookup[(destination[0], destination[1])] != float(
            "inf") else -1

    def shortestDistance2(self, maze, start, destination):
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return -1
        maze = [[1] * (len(maze[0]) + 2)] + [[1] + m + [1] for m in maze] + [[1] * (len(maze[0]) + 2)]
        # visited = {(start[0] + 1, start[1] + 1)}
        lookup = {}

        # @lru_cache(None)
        def dfs(i, j, visited):
            if i == destination[0] + 1 and j == destination[1] + 1:
                return 0
            if (i, j) in lookup:
                return lookup[(i, j)]
            res = float("inf")
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                tmp_i = i
                tmp_j = j
                while maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                    # print(tmp_i, tmp_j, x, y)
                if (tmp_i, tmp_j) not in visited:
                    # visited.add((tmp_i, tmp_j))
                    res = min(res, abs(tmp_i - i) + abs(tmp_j - j) + dfs(tmp_i, tmp_j, visited | {(tmp_i, tmp_j)}))
                    # visited.remove((tmp_i, tmp_j))
            lookup[(i, j)] = res
            return res

        tmp = dfs(start[0] + 1, start[1] + 1, {(start[0] + 1, start[1] + 1)})
        print(lookup)
        return tmp if tmp != float("inf") else -1

    def shortestDistance4(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        from functools import lru_cache
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return -1
        maze = [[1] * (len(maze[0]) + 2)] + [[1] + m + [1] for m in maze] + [[1] * (len(maze[0]) + 2)]
        visited = {(start[0] + 1, start[1] + 1)}

        @lru_cache(None)
        def dfs(i, j):
            if i == destination[0] + 1 and j == destination[1] + 1:
                return 0
            res = float("inf")
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                tmp_i = i
                tmp_j = j
                while maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                    # print(tmp_i, tmp_j, x, y)
                if (tmp_i, tmp_j) not in visited:
                    visited.add((tmp_i, tmp_j))
                    res = min(res, abs(tmp_i - i) + abs(tmp_j - j) + dfs(tmp_i, tmp_j))
                    visited.remove((tmp_i, tmp_j))
            return res

        tmp = dfs(start[0] + 1, start[1] + 1)
        return tmp if tmp != float("inf") else -1

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        import heapq
        maze = [[1] * (len(maze[0]) + 2)] + [[1] + m + [1] for m in maze] + [[1] * (len(maze[0]) + 2)]
        visited = set()

        heap = [[0, start[0] + 1, start[1] + 1]]

        while heap:

            step, i, j = heapq.heappop(heap)

            if (i, j) in visited:
                continue
            if i == destination[0] + 1 and j == destination[1] + 1:
                return step
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                tmp_i = i
                tmp_j = j
                while maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                    # print(tmp_i, tmp_j, x, y)
                heapq.heappush(heap, [step + abs(tmp_i - i) + abs(tmp_j - j), tmp_i, tmp_j])
            visited.add((i, j))
        return -1

a = Solution()
print(a.shortestDistance2([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4],
                          [4, 4]))
print(a.shortestDistance(
    [[0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0]]
    , [0, 0]
    , [8, 6]))

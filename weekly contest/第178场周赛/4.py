from typing import List


class Solution:
    def minCost1(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq
        lookup = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0]
        }
        dis = defaultdict(lambda: float("inf"))
        row = len(grid)
        col = len(grid[0])
        queue = [(0, 0, 0)]
        dis[(0, 0)] = 0
        while queue:
            # print(queue)
            cost, i, j = heapq.heappop(queue)
            for k, v in lookup.items():
                tmp_i = i + v[0]
                tmp_j = j + v[1]
                if 0 <= tmp_i < row and 0 <= tmp_j < col:
                    ncost = cost
                    if k != grid[i][j]: ncost += 1
                    if dis[(tmp_i, tmp_j)] > ncost:
                        dis[(tmp_i, tmp_j)] = ncost
                        heapq.heappush(queue, (ncost, tmp_i, tmp_j))
        # print(dis)
        return dis[(row - 1, col - 1)]

    def minCost(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        lookup = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0]
        }
        dis = defaultdict(lambda: float("inf"))
        row = len(grid)
        col = len(grid[0])
        bfs = []
        k = 0

        def dfs(i, j):
            if not (0 <= i < row and 0 <= j < col and dis[(i, j)] == float("inf")): return
            dis[(i, j)] = k
            bfs.append((i, j))
            dfs(i + lookup[grid[i][j]][0], j + lookup[grid[i][j]][1])

        dfs(0, 0)
        while bfs:
            k += 1
            bfs, nxt = [], bfs
            for i, j in nxt:
                for x, y in lookup.values():
                    dfs(i + x, j + y)

        return dis[(row - 1, col - 1)]


a = Solution()
print(a.minCost(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))
# print(a.minCost(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]))
# print(a.minCost(grid=[[1, 2], [4, 3]]))
print(a.minCost(grid=[[4]]))
# print(a.minCost(
#     [[3, 4, 3], [2, 2, 2], [2, 1, 1], [4, 3, 2], [2, 1, 4], [2, 4, 1], [3, 3, 3], [1, 4, 2], [2, 2, 1], [2, 1, 1],
#      [3, 3, 1], [4, 1, 4], [2, 1, 4], [3, 2, 2], [3, 3, 1], [4, 4, 1], [1, 2, 2], [1, 1, 1], [1, 3, 4], [1, 2, 1],
#      [2, 2, 4], [2, 1, 3], [1, 2, 1], [4, 3, 2], [3, 3, 4], [2, 2, 1], [3, 4, 3], [4, 2, 3], [4, 4, 4]]))

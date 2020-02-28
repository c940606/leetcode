from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        heap = []
        cur_max = float("-inf")
        visited = set()
        row = len(heightMap)
        col = len(heightMap[0])
        res = 0
        # 边界放进去
        # 行
        for j in range(col):
            heapq.heappush(heap, [heightMap[0][j], 0, j])
            heapq.heappush(heap, [heightMap[row - 1][j], row - 1, j])
            visited.add((0, j))
            visited.add((row - 1, j))
        # 列
        for i in range(row):
            heapq.heappush(heap, [heightMap[i][0], i, 0])
            heapq.heappush(heap, [heightMap[i][col - 1], i, col - 1])
            visited.add((i, 0))
            visited.add((i, col - 1))

        while heap:
            h, i, j = heapq.heappop(heap)
            cur_max = max(h, cur_max)
            for s, t in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = i + s
                tmp_j = j + t
                if tmp_i < 0 or tmp_i >= row or tmp_j < 0 or tmp_j >= col or (tmp_i, tmp_j) in visited:
                    continue
                visited.add((tmp_i, tmp_j))
                if heightMap[tmp_i][tmp_j] < cur_max:
                    res += cur_max - heightMap[tmp_i][tmp_j]
                heapq.heappush(heap, [heightMap[tmp_i][tmp_j], tmp_i, tmp_j])
        return res


a = Solution()
print(a.trapRainWater([
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]))
print(a.trapRainWater([
    [3, 10, 8, 12, 2, 7, 9],
    [7, 1, 11, 3, 8, 1, 10],
    [9, 7, 3, 10, 2, 5, 6],
    [7, 11, 1, 4, 6, 11, 9],
    [4, 5, 8, 12, 3, 4, 2],
    [12, 2, 12, 1, 5, 9, 6],
    [6, 5, 8, 12, 4, 11, 10]
]))
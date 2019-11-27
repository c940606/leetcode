from typing import List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        t = [[0] * m for _ in range(n)]
        for x, y in indices:
            for j in range(m):
                t[x][j] += 1
            for i in range(n):
                t[i][y] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if t[i][j] % 2 == 1:
                    res += 1
        return res

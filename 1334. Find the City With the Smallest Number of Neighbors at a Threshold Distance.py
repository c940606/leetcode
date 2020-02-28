from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = [[float("inf")] * n for _ in range(n)]
        for fm, to, wg in edges:
            mat[fm][to] = wg
            mat[to][fm] = wg
        for i in range(n):
            mat[i][i] = 0
        # print(mat)
        res = [0] * n
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

        for i in range(n):
            for j in range(i+1, n):
                if mat[i][j] <= distanceThreshold:
                    res[i] += 1
                    res[j] += 1
        _min = min(res)
        for i in range(n - 1, -1, -1):
            if res[i] == _min:
                return  i

a = Solution()
print(a.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
print(a.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))
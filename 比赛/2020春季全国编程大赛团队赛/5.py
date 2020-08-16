from typing import List


class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:

        def cross_mul(x, y):
            print(x, y)
            return x[0] * y[1] - x[1] * y[0]

        p = 0
        for i in range(1, len(points)):
            if points[i][1] < points[p][1] or points[i][1] == points[p][1] and points[i][0] < points[p][0]:
                p = i
        res = []
        res.append(p)
        visited = set()
        visited.add(p)
        for s in direction:
            x = -1
            for j in range(len(points)):
                if j not in visited:
                    if x == -1:
                        x = j
                    if s == "L":
                        if cross_mul([points[j][0] - points[p][0], points[j][1] - points[p][1]],
                                     [points[x][0] - points[p][0], points[x][1] - points[p][1]]) > 0:
                            x = j

                    if cross_mul([points[j][0] - points[p][0], points[j][1] - points[p][1]],
                                 [points[x][0] - points[p][0], points[x][1] - points[p][1]]) < 0:
                        x = j
            res.append(x)
            visited.add(x)
            p= x
        return res
a = Solution()
print(a.visitOrder(points = [[1,1],[1,4],[3,2],[2,1]], direction = "LL"))



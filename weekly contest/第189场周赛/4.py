from typing import List


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        import math

        eps = 10 ** (-8)

        def dis(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        # print(dis([0, 1], [1, 0]))
        # print(dis([-3, 0], [7, 8]))

        def getcenter(p1, p2):
            mid = [0, 0]
            mid[0], mid[1] = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            angle = math.atan2(p1[0] - p2[0], p2[1] - p1[1])
            tmp = dis(p1, mid)
            # print(r, tmp, p1, p2)
            d = math.sqrt(r ** 2 - tmp ** 2)
            return [mid[0] + d * math.cos(angle), mid[1] + d * math.sin(angle)]

        res = 1

        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                if i == j or dis(points[i], points[j]) > 2.0 * r: continue
                cnt = 0
                center = getcenter(points[i], points[j])
                for k in range(n):
                    if dis(points[k], center) < 1.0 * r + eps : cnt += 1
                res = max(cnt, res)
        return res


a = Solution()
print(a.numPoints(points=[[-2, 0], [2, 0], [0, 2], [0, -2]], r=2))
print(a.numPoints(points=[[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r=5))
print(a.numPoints( points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1))
print(a.numPoints(points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2))
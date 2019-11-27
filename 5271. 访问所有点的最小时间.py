from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        s1, s2 = points[0]
        res = 0
        for x, y in points[1:]:
            res += max(abs(s1 - x), abs(s2 - y))
            s1, s2 = x, y
        return res



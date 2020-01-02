import bisect
from typing import List


class Solution:
    def removeInterval1(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        left = bisect.bisect_left(intervals, [toBeRemoved[0]])
        right = bisect.bisect_left(intervals, [toBeRemoved[1]])

        res = []

        res += [intervals[:left]]
        if res and res[-1][1] >= toBeRemoved[0]:
            res += [[res.pop()[0], toBeRemoved[0]]]
        if right > 0 and intervals[right - 1][1] > toBeRemoved[1]:
            res += [[toBeRemoved[1], intervals[right - 1][1]]]
        res.extend(intervals[right:])
        return res

    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        res = []

        def helper(a, b):
            if b[1] <= a[0]:
                return [a]
            elif a[0] < b[1] < a[1]:
                if b[0] <= a[0]:
                    return [[b[1], a[1]]]
                elif b[0] > a[0]:
                    return [[a[0], b[0]], [b[1], a[1]]]
            else:
                if b[0] < a[0]:
                    return []
                elif b[0] > a[1]:
                    return [a]
                else:
                    return [[a[0], b[0]]]

        for interval in intervals:
            res += helper(interval, toBeRemoved)
        return res

        # if left == 0:
        #     if intervals[0][0] >= toBeRemoved[0]:
        #         left = -1

        # if intervals[left - 1][1] >= toBeRemoved[0]:
        #     left -= 1
        # if intervals[right - 1][1] >= toBeRemoved[1]:
        #     right -= 1
        # print(left, right)
        # if left == -1 and right == -1:
        #     return intervals
        # if left == -1 and right == n:
        #     return []
        # if left == -1:
        #     return [[toBeRemoved[1], intervals[right][1]]] + intervals[right + 1:]
        # if left == n and right == n:
        #     return intervals
        #
        # if right == n:
        #     return intervals[:left] + [[intervals[left][0], toBeRemoved[0]]]
        #
        # return intervals[:left] + [[toBeRemoved[1], intervals[right][1]]] + intervals[right + 1:]


a = Solution()
print(a.removeInterval([[0, 2]], [7, 8]))
print(a.removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]))
print(a.removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[7, 8]))
print(a.removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[3, 4]))
print(a.removeInterval([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]))
print(a.removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]))

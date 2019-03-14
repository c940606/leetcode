# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        lookup = []
        for idx, val in enumerate(intervals):
            lookup.append((val.start, idx))
        lookup.sort()
        n = len(lookup)

        def helper(x):
            lo = 0
            hi = n
            while lo < hi:
                mid = (lo + n) // 2
                if lookup[mid][0] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        res = []

        for interval in intervals:
            idx = helper(interval.end)
            if idx == n:
                res.append(-1)
            elif idx == 0:
                if interval.end <= lookup[0][0]:
                    res.append(lookup[0][1])
                else:
                    res.append(-1)
            else:
                res.append(lookup[idx][1])
        return res

    def findRightInterval1(self, intervals):
        import bisect
        lookup = []
        for idx, val in enumerate(intervals):
            lookup.append((val[0], idx))
        lookup.sort()
        n = len(lookup)
        # print(intervals)
        # print(lookup)
        # def helper(x):
        #     lo = 0
        #     hi = n
        #     while lo < hi:
        #         mid = (lo + hi) // 2
        #         if lookup[mid][0] < x:
        #             lo = mid + 1
        #         else:
        #             hi = mid
        #     return lo

        res = []

        for interval in intervals:
            # idx = helper(interval[1])
            idx = bisect.bisect_left(lookup, (interval[1],))
            print(interval, idx)

            if idx == n:
                res.append(-1)
            elif idx == 0:
                if interval.end <= lookup[0][0]:
                    res.append(lookup[0][1])
                else:
                    res.append(-1)
            else:
                res.append(lookup[idx][1])
        return res


a = Solution()
print(a.findRightInterval1([[3, 4], [2, 3], [1, 2]]))

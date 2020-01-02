class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev = intervals[0]
        cnt = 1
        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][1]:
                continue
            prev = intervals[i]
            cnt += 1
        return cnt

a = Solution()
print(a.removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8], [1, 2]]))

class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        while i < n and newInterval[0] > intervals[i][1]:
            i += 1
        left = i
        while i < n and newInterval[1] >= intervals[i][0]:
            i += 1
        right = i
        print(left, right)
        if left >= n:
            res = intervals + [newInterval]
        elif left == right:
            # print(intervals)
            intervals.insert(left, newInterval)
            res = intervals
        else:
            res = intervals[:left] + [
                [min(intervals[left][0], newInterval[0]), max(intervals[right - 1][1], newInterval[1])]] + intervals[
                                                                                                           right:]
        return res

    def insert1(self, intervals, newInterval):
        if not intervals: return [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]: return intervals + [newInterval]
        i = 0
        n = len(intervals)

        while i < n and newInterval[0] > intervals[i][1]:
            i += 1
        left = min(intervals[i][0], newInterval[0])
        tmp = i
        # print(tmp)
        if intervals[i][0] > newInterval[1]:
            return intervals[:tmp] + [newInterval] + intervals[tmp:]
        right = max(intervals[i][1], newInterval[1])
        #print(tmp)

        while i < n and newInterval[1] >= intervals[i][0]:
            right = max(right, intervals[i][1])
            i += 1
        #print(tmp, i)
        return intervals[:tmp] + [[left, right]] + intervals[i:]


a = Solution()
# print(a.insert1(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
# print(a.insert1(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
# print(a.insert1([[1, 5]], [6, 8]))
# print(a.insert([[1, 5]], [0, 0]))
# print(a.insert1([[1, 5]], [0, 3]))
print(a.insert1([[3, 5], [12, 15]], [6, 6]))

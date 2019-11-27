from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort()
        rooms = 1
        q_times = [intervals[0][1]]

        for x, y in intervals[1:]:
            if x >= q_times[0]:
                heapq.heappop(q_times)
            else:
                rooms += 1
            heapq.heappush(q_times, y)
        return rooms


a = Solution()
print(a.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(a.minMeetingRooms([[7, 10], [2, 4]]))

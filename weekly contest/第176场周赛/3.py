from typing import List
from collections import defaultdict, deque

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq
        heapq.heapify(events)
        # events.sort()
        # time = events[0][0] + 1
        # res = 1
        # #print(events)
        # for start, end in events[1:]:
        #     #print(time, start, end)
        #     if time > end:
        #         continue
        #     res += 1
        #     time = max(time + 1, start + 1)
        #
        # return res
        time = 0
        res = 0
        while events:
            start, end = heapq.heappop(events)
            if time > end:continue
            if start < time:
                heapq.heappush(events, [time, end])
                continue
            res += 1
            time = max(time, start) + 1
        return res

a = Solution()
print(a.maxEvents([[1,2],[2,3],[3,4]]))
print(a.maxEvents([[1,2],[2,3],[3,4],[1,2]]))
print(a.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))
print(a.maxEvents([[1,100000]]))
print(a.maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]))
print(a.maxEvents([[1,2],[2,2],[3,3],[3,4],[3,4]]))
print(a.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])) # 5
from typing import List


class Solution:
    def minTaps(self, n: int, _ranges: List[int]) -> int:
        from collections import deque
        interval = []
        for idx, val in enumerate(_ranges):
            interval.append([idx - val, idx + val])
        interval.sort()
        interval = deque(interval)
        # print(interval)
        queue = deque()
        left = 0
        if interval[0][0] > 0:
            return -1
        while interval and interval[0][0] <= left:
            queue.appendleft([interval.popleft()[1], 1])

        while queue:
            left, step = queue.pop()
            if left >= n: return step
            while interval and interval[0][0] <= left:
                queue.appendleft((interval.popleft()[1], step + 1))

        return -1


a = Solution()
# print(a.minTaps(5,  [3,4,1,1,0,0]))
# print(a.minTaps(3,[0,0,0,0]))
print(a.minTaps(n=7, _ranges=[1, 2, 1, 0, 2, 1, 0, 1]))
print(a.minTaps(n=8, _ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]))
print(a.minTaps(n=8, _ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]))

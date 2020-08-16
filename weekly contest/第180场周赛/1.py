from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        import bisect

        queue = []
        res = 0
        cur = 0
        for x, y in sorted(zip(efficiency, speed), reverse=True):
            cur += y
            bisect.insort(queue, -y)
            if len(queue) > k:
                cur += queue.pop()
            res = max(res, x * cur)
        return res

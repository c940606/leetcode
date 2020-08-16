from typing import List


class Solution:
    def shortestSubarray1(self, A: List[int], K: int) -> int:
        import bisect
        q = [[0, -1]]
        cur = 0
        res = float("inf")
        for idx, val in enumerate(A):

            cur += val
            # print(q, cur)
            target = cur - K
            loc = bisect.bisect_left(q, [target + 1]) - 1
            # print(loc)
            if loc != -1:
                # print(loc)
                res = min(res, idx - max(q[:loc + 1], key=lambda x: x[1])[1])
            bisect.insort(q, [cur, idx])
        return res

    def shortestSubarray(self, A: List[int], K: int) -> int:
        import heapq
        heap = [[0, -1]]
        cur = 0
        res = float("inf")
        for idx, val in enumerate(A):
            cur += val
            while heap and cur - heap[0][0] >= K:
                res = min(res, idx - heapq.heappop(heap)[1])
            heapq.heappush(heap, [cur, idx])
        return res



a = Solution()
print(a.shortestSubarray(A=[2, -1, 2], K=3))

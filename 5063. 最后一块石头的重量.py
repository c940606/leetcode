class Solution:
    def lastStoneWeight(self, stones) -> int:
        import bisect
        stones.sort()
        while stones:
            a = stones.pop(-1)
            if not stones:
                return a
            b = stones.pop(-1)
            bisect.insort_left(stones, abs(a - b))
        return 0

    def lastStoneWeight1(self, stones) -> int:
        import heapq
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        for i in range(len(stones) - 1):
            a, b = -heapq.heappop(stones), -heapq.heappop(stones)
            heapq.heappush(stones, -abs(a - b))
        return -stones[0]


a = Solution()
print(a.lastStoneWeight([1, 2, 3, 1]))

from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        import heapq
        heapq.heapify(nums)
        n = len(nums)
        res = 0
        while len(set(nums)) >  1:
            tmp = []
            for _ in range(n - 1):
                tmp.append(heapq.heappop(nums) + 1)
            for t in tmp:
                heapq.heappush(nums, t)
            res += 1
        return res
a = Solution()
print(a.minMoves([1,2,3]))
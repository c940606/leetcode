from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        import heapq
        target = [-t for t in target]
        heapq.heapify(target)
        while True:
            num = heapq.heappop(target)
            if num == -1: return True
            if num  - sum(target) > 0:return False
            heapq.heappush(target, num - sum(target))

a = Solution()
print(a.isPossible([9, 3, 5]))
print(a.isPossible(target = [8,5]))
print(a.isPossible([1,1,1,2]))
print(a.isPossible([9,9, 9]))
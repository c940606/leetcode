import collections
from typing import List


class Solution:
	def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
		import heapq
		c = collections.Counter(arr)
		res = len(c)
		heap = []
		for k1, v in c.items():
			heapq.heappush(heap, [v, k1])
		# print(heap)
		while k:
			v, k1 = heapq.heappop(heap)
			v -= 1
			k -= 1
			if v == 0:
				res -= 1
				continue
			heapq.heappush(heap, [v, k1])
		return res


a = Solution()
print(a.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
print(a.findLeastNumOfUniqueInts([5,5,4],
1))

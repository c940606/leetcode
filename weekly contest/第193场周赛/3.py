from typing import List
import collections


class Solution:
	def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
		from itertools   import groupby
		n = len(bloomDay)
		if m * k > n: return -1
		if m * k == n: return max(bloomDay)
		left = min(bloomDay)
		right = max(bloomDay)
		def cal(mid):
			tmp = [0] * n
			ans = 0
			for idx, day in enumerate(bloomDay):
				if day <= mid:
					tmp[idx] = 1
			print(mid, tmp)
			for k1, v in groupby(tmp):
				if k1 == 1:
					ans += len(list(v)) // k
			return ans



		while left < right:
			mid = (left +right) // 2
			print(mid, cal(mid))
			if cal(mid) < m:
				left = mid + 1
			else:
				right = mid
		return left

a = Solution()
# print(a.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
print(a.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
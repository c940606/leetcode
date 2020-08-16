from typing import List


class Solution:
	def minDistance(self, houses: List[int], k: int) -> int:
		import functools
		houses.sort()
		n = len(houses)

		def cal(pre, j):
			ans = 0
			while pre < j:
				ans += houses[j] - houses[pre]
				j -= 1
				pre += 1
			return ans

		@functools.lru_cache(None)
		def dfs(pre, cur, k):
			# print(pre, cur, k)
			if k < 0:
				return float("inf")


			if pre == len(houses):
				if k > 0:
					return float("inf")
				else:
					return 0
			if cur >= n: return float("inf")
			res = float("inf")
			res = min(res, dfs(pre, cur + 1, k), cal(pre, cur) + dfs(cur + 1, cur + 1, k - 1))

			return res

		return dfs(0, 0, k)

a = Solution()
print(a.minDistance(houses = [1,4,8,10,20], k = 3))
print(a.minDistance(houses = [7,4,6,1], k = 1))
print(a.minDistance(houses = [2,3,5,12,18], k = 2))
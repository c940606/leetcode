class Solution(object):
	def canReorderDoubled(self, A):
		"""
		:type A: List[int]
		:rtype: bool
		"""
		from collections import Counter
		A.sort(key=lambda x: abs(x))
		c = Counter(A)

		for i in range(len(A)):
			if c[A[i]] == 0: continue
			if c[A[i] * 2] == 0:
				return False
			c[A[i]] -= 1
			c[2 * A[i]] -= 1
		return True


a = Solution()
print(a.canReorderDoubled([4, -2, 2, -4]))
# print(a.canReorderDoubled([3,1,3,6]))
# print(a.canReorderDoubled([1,2,4,8]))
# print(a.canReorderDoubled([0,0]))
# print(a.canReorderDoubled([2,1,2,1,1,1,2,2]))
# print(a.canReorderDoubled([1, 2, 4, 16, 8, 4]))

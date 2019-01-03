class Solution:
	def repeatedNTimes(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		from collections import defaultdict
		lookup = defaultdict(int)
		n = len(A)
		for a in A:
			lookup[a] += 1
			if lookup[a] == n // 2:
				return a
a = Solution()
print(a.repeatedNTimes([5,1,5,2,5,3,5,4]))
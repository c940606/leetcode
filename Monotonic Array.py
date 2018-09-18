class Solution(object):
	def isMonotonic(self, A):
		"""
		如果数组是单调递增或单调递减的，那么它是单调的。
		如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。
		如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
		当给定的数组 A 是单调数组时返回 true，否则返回 false。
		----
		输入：[1,2,2,3]
		输出：true
		---
		输入：[6,5,4,4]
		输出：true
		---
		先判断是递增还是递减的
		:type A: List[int]
		:rtype: bool
		"""
		i = 0
		j = 1
		n = len(A)
		while j < n and A[i] == A[j]:
			i += 1
			j += 1
		if j >= n:
			return True
		print(i,j)
		if A[i] < A[j]:
			while j < n:
				if A[i] > A[j]:
					return False
				i += 1
				j += 1
			return True
		else:
			while j < n:
				if A[i] < A[j]:
					return False
				i += 1
				j += 1
			return True
a = Solution()
print(a.isMonotonic([-5,-5,-5,-5,-2,-2,-2,-1,-1,-1,0]))
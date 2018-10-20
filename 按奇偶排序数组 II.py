class Solution(object):
	def sortArrayByParityII(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		n = len(A)
		res = [None]*n
		odd = 1
		even = 0
		i = 0
		while i < n:
			if A[i] %2 == 0:
				res[even] = A[i]
				even += 2
			else:
				res[odd] = A[i]
				odd += 2
			i += 1
		return res

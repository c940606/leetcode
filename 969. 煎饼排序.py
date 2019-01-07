class Solution(object):
	def pancakeSort(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		res = []
		n = len(A)
		while n :
			idx = A.index(n)
			print("idx:",idx)
			res.append(idx+1)
			A = A[:idx+1][::-1]+A[idx+1:]
			print(A)
			res.append(n)
			A = A[:n][::-1]+A[n:]
			print(A)
			n -= 1
			# A = A[:idx+1][::-1][::-1]
		print(A)
		return res

a = Solution()
print(a.pancakeSort([3,2,4,1]))
print(a.pancakeSort([1,2,3]))
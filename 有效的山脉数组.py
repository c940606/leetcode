class Solution(object):
	def validMountainArray(self, A):
		"""
		:type A: List[int]
		:rtype: bool
		"""
		n = len(A)
		if n < 3:
			return False
		i = 0
		if A[i] > A[i+1]:
			return False
		while True:
			while i < n-1 and A[i] <= A[i+1]:
				i += 1
			print(i)
			if i == n -1:
				return False

			while True:
				if i == n-1:
					return True
				if i < n-1 and A[i] > A[i+1]:
					i +=1
				else:
					return False
a = Solution()
# print(a.validMountainArray([0,3,2,1]))
print(a.validMountainArray([9,8,7,6,5,4,3,2,1,0]))

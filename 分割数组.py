class Solution(object):
	def partitionDisjoint(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		if not A:
			return 0
		n = len(A)

		left_min = [A[0]]
		right_min = [A[-1]]
		for i in range(1,n):
			left_min.append(max(left_min[-1],A[i]))
		print(left_min)
		for j in range(n-2,-1,-1):
			right_min.append(min(right_min[-1],A[j]))
		print(right_min[::-1])
		right_min = right_min[::-1]
		for k in range(n-1):
			if left_min[k] <= right_min[k+1]:
				return k+1
		return 0



a = Solution()
print(a.partitionDisjoint([1,1,1,0,6,12]))
print(a.partitionDisjoint([5,0,3,8,6]))


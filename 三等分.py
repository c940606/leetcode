class Solution(object):
	def threeEqualParts(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		if not A:
			return [-1,-1]
		n = len(A)
		def helper(t_bin):

			return "".join(map(str,t_bin))
		for i in range(n-1):
			# if helper(A[:i+1]) > helper(A[i+1:]):
			# 	break
			for j in range(i+2,n):
				print(A[:i+1],A[i+1:j],A[j:])
				# print(i,j)
				temp1 = helper(A[:i+1])
				temp2 = helper(A[i+1:j])
				temp3 = helper(A[j:])
				if temp1 == temp2 and temp2 == temp3:
					return [i,j]
				elif temp1 != temp2 or temp1 != temp3:
					break
		return [-1,-1]

	def threeEqualParts1(self, A):
		total = sum(A)
		n = len(A)
		if total % 3 != 0:
			return [-1,-1]
		if total == 0:
			return [0,n-1]
		total /= 3
		count = 0
		now = ""
		for i in range(n-1,-1,-1):
			now = str(A[i]) + now
			if A[i] == 1:
				count += 1
				if count == total:
					break
		A = "".join(map(str,A))
		print(A,now)
		tmp = A.find(now)
		if tmp == -1 or tmp == n - len(now):
			return [-1,-1]
		l = tmp + len(now) - 1
		A = A[l+1:]
		tmp = A.find(now)
		if tmp == -1 or tmp == n - len(now):
			return [-1,-1]
		r = tmp + len(now) + 1
		return [l,r+1]

a = Solution()
print(a.threeEqualParts1([1,0,1,0,1]))
print(a.threeEqualParts1([1,1,0,1,1]))
print(a.threeEqualParts1([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]))





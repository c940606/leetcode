class Solution(object):
	def largestTimeFromDigits(self, A):
		"""
		:type A: List[int]
		:rtype: str
		"""
		if min(A) > 2:
			return ""
		if max(A) == 0:
			return "00:00"
		A = sorted(A,reverse=True)
		res = []
		miute = []
		visited = [0] *4
		for i in range(4):
			print(A[i])
			if  0<=A[i] <=2 and not visited[i]:
				visited[i] = 1
				res.append(A[i])
				continue
			if 2 <A[i] <= 3 and not visited[i]:
				visited[i] = 1
				res.append(A[i])
				continue
			if 3< A[i] <= 5 and not visited[i]:
				visited[i] = 1
				miute.append(A[i])
				continue
			else:
				miute.append(A[i])

		print(res,miute)

	def largestTimeFromDigits1(self, A):
		if min(A) > 2:
			return ""
		if max(A) == 0:
			return "00:00"
		# 时
		copy_A = A.copy()
		res = []
		if 2 in A:
			res.append(2)
			A.remove(2)
			if min(A) > 3:
				return ""
			temp = 3
			while temp not in A:
				temp -= 1
			res.append(temp)
			A.remove(temp)
			A = sorted(A,reverse=True)
			if min(A) <= 5:

				if A[0] > 5:
					A[0],A[1] = A[1],A[0]
				return "".join(map(str,res))+":" + "".join(map(str,A))
		print("---")
		A = copy_A.copy()
		res = []
		if 1 in A:
			res.append(1)
			A.remove(1)
			temp = 9
			while temp not in A:
				temp -= 1
			res.append(temp)
			A.remove(temp)
			A = sorted(A, reverse=True)
			if min(A) <=  5:

				if A[0] > 5:
					A[0],A[1] = A[1],A[0]
				# print(res, A)
				return "".join(map(str, res)) + ":" + "".join(map(str, A))
		print("----")
		A = copy_A.copy()
		res = []
		if 0 in A:
			res.append(0)
			A.remove(0)
			temp = 9
			while temp not in A:
				temp -= 1
			res.append(temp)
			A.remove(temp)
			A = sorted(A, reverse=True)
			print(res,A)
			if min(A) <=  5:

				if A[0] > 5:
					A[0],A[1] = A[1],A[0]
				# print(res, A)
				return "".join(map(str, res)) + ":" + "".join(map(str, A))

	def largestTimeFromDigits2(self, A):
		if min(A) > 2:
			return ""
		if max(A) == 0:
			return "00:00"
		res = [0,0,0,0]
		A.sort()
		for hour in range(23,-1,-1):
			for minute in range(59,-1,-1):
				res[0] = hour//10
				res[1] = hour% 10
				res[2] = minute//10
				res[3] = minute%10
				# print(res,A)
				if sorted(res) == A:
					res = list(map(str,res))
					return "".join(res[:2])+":"+"".join(res[2:])
		return ""







a = Solution()
print(a.largestTimeFromDigits2([1,2,3,4]))
# print(a.largestTimeFromDigits([5,5,5,5]))
# print(a.largestTimeFromDigits1([0,0,1,0]))
# print(a.largestTimeFromDigits1([0,4,0,0]))
# print(a.largestTimeFromDigits1([4,2,4,4]))
# print(a.largestTimeFromDigits1([1,9,6,0]))
# print(a.largestTimeFromDigits1([2,0,6,6]))


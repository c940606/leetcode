class Solution(object):
	def numberOfArithmeticSlices(self, A):
		"""
		如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
		例如，以下数列为等差数列:
		1, 3, 5, 7, 9
		7, 7, 7, 7
		3, -1, -5, -9
		:type A: List[int]
		:rtype: int
		"""

		n = len(A)
		if n < 3:
			return 0
		res =[0]*n
		flag = A[1] - A[0]
		i = 2
		while i < n:
			temp = A[i] - A[i-1]
			if temp == flag :
				res[i] = res[i-1]+1
			else:
				flag = temp
			i += 1
			print(res)
		return sum(res)
a = Solution()
print(a.numberOfArithmeticSlices([1,2,3,4,5,7]))

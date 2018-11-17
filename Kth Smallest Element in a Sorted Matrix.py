class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
		请注意，它是排序后的第k小元素，而不是第k个元素。
		---
		matrix = [
				   [ 1,  5,  9],
				   [10, 11, 13],
				   [12, 13, 15]
				],
		k = 8,
		返回 13。
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		self.n = len(matrix)
		left = matrix[0][0]
		right = matrix[self.n-1][self.n-1]
		# print(left,right)
		while left<right:
			mid = (left+right)//2
			num = self.search_less_equal(matrix,mid)
			# print(mid,num)
			if (num < k):
				left = mid+1
			else:
				right = mid
		return left
	def search_less_equal(self,matrix,target):
		self.n = len(matrix)
		i = self.n - 1
		j = 0
		res = 0
		while i>=0 and j< self.n:
			if matrix[i][j] <=target:
				res += i+1
				j += 1
			else:
				i -= 1
		return res
a = Solution()
print(a.kthSmallest([
				   [ 1,  5,  9],
				   [10, 11, 13],
				   [12, 13, 15]
				],8))

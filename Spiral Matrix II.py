class Solution:
	def generateMatrix(self, n):
		"""
		给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
		:type n: int
		:rtype: List[List[int]]
		"""
		matrix = [[0]*n for _ in range(n)]
		i = 0
		j = 0
		step = 0
		nums = [i+1 for i in range(n*n)]
		k = 0
		while k < n*n:
			if i == step :
				matrix[i][j] =nums[k]
				j += 1
				k += 1
				# print(j)
				# print(n-step)
				if j == n-step:
					i += 1
					j = n-step-1
				# print(matrix)
			elif j == n-step-1:
				matrix[i][j] = nums[k]
				i += 1
				k += 1
				if i == n-step:
					j -= 1
					i = n-1-step
				# print(matrix)
			elif i == n-1-step:
				matrix[i][j] = nums[k]
				j -= 1
				k += 1
				if j == step-1:
					i -= 1
					j = step
				# print(matrix)
			elif j == step:
				matrix[i][j] = nums[k]
				k += 1
				i -= 1
				if i == step:
					j += 1
					i = step+1
				# print(matrix)
			else:
				step += 1

		return matrix
a = Solution()
print(a.generateMatrix(4))




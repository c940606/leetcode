class Solution:
	def spiralOrder(self, matrix):
		"""
		给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素
		----
		输入:
			[
			 [ 1, 2, 3 ],
			 [ 4, 5, 6 ],
			 [ 7, 8, 9 ]
			]
			输出: [1,2,3,6,9,8,7,4,5]
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		self.res = []
		#外侧输出
		# print(matrix)
		self.outer(matrix)
		# print(self.res)
		#内侧矩阵
		# self.inter(matrix)
		while matrix:
			print(matrix)
			matrix = self.inter(matrix)
			print(self.res)
			if len(matrix)==0 or len(matrix[0])==0:
				self.outer(matrix)
			else:
				break

		return self.res

	def outer(self,matric):
		# print(matric)
		i = 0
		j = 0
		# print(matric[0])
		ni = len(matric)
		nj = len(matric[0])
		# print(ni,nj)
		if ni == 1 :
			self.res += matric[0]
		elif nj ==1 :
			for item in matrix:
				self.res += item
		else:
			while not (i == 1 and j == 0):
				if i == 0:
					self.res.append(matric[i][j])
					# self.res
					# print(self.res)
					j += 1
					if j == nj:
						i += 1
						j = j-1
				elif j == nj-1:
					self.res.append(matric[i][j])
					i += 1
					if i == ni:
						i = i-1
						j -= 1
				elif i == ni-1:
					self.res.append(matric[i][j])
					j -= 1
					if j == -1:
						j = 0
						i -= 1
				elif j == 0:
					self.res.append(matric[i][j])
					i -= 1

			self.res.append(matric[1][0])
		# if ni > 1 :
		# 	self.res.append(matric[1][0])



	def inter(self,matrix):
		matrix =list(map(lambda x:x[1:-1],matrix[1:-1]) )
		# print(matrix)
		return matrix
	def spiralOrder1(self, matrix):
		res = []
		while matrix:
			res += matrix.pop(0)
			if matrix ==[]:
				break
			print(res,matrix)
			res += list(map(lambda x:x.pop(-1),matrix))
			print(res,matrix)
			if matrix ==[] or matrix[0]==[]:
				break
			res += matrix.pop(-1)[::-1]
			if matrix ==[] or matrix[0]==[]:
				break
			res += list(map(lambda x: x.pop(0), matrix[::-1]))
			if matrix ==[] or matrix[0]==[]:
				break
		return res




matrix = [
			 [ 1, 2, 3 ],
			 [ 4, 5, 6 ],
			 [ 7, 8, 9 ]
			]
matrix2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
matrix3 = [[3],[2]]
matrix4 = [[6,7]]
matrix1 = [[5]]
matrix5 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
matrix6 = [[1,11],
		   [2,12],
		   [3,13],
		   [4,14],
		   [5,15],
		   [6,16],
		   [7,17],
		   [8,18],
		   [9,19],
		   [10,20]]
a = Solution()
print(a.spiralOrder1(matrix))
# print(a.outer([[5]]))




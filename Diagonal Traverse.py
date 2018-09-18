class Solution(object):
	def findDiagonalOrder(self, matrix):
		"""
		给定一个含有 M x N 个元素的矩阵（M行，N列），
		请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
		----
		输入:
			[
			 [ 1, 2, 3 ],
			 [ 4, 5, 6 ],
			 [ 7, 8, 9 ]
			]
			输出:  [1,2,4,7,5,3,6,8,9]
		---
		思路:
		可以把每一斜线的 列表找出来
		然后 根据取反,取正这样输出
		1.然后把斜线列表找出来?
			规律:纵横坐标加起来0,1,2,首先把坐标找出来
			注意点:纵横坐标不能超过矩阵的标准
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		m = len(matrix)
		n = len(matrix[0])
		max_mn = m+n-1
		# i = 0
		# j = 0
		res_index = []
		print(max_mn)
		flag = 0
		for sum_ij in range(max_mn):

			i = flag
			j = sum_ij - flag
			if j == n:
				flag += 1
				i = flag
				j = sum_ij-flag
				# print("j==n:",i,j)
			# if i == m:
			# 	j -= 1
			# 	i = sum_ij -j
			temp = []
			# print(i, j)
			# print("----")
			while 0 <=i< m and 0 <=j< n:

				temp.append(matrix[i][j])
				i += 1
				j -= 1
				# print(i, j)

			res_index.append(temp)
		l = len(res_index)
		res = []
		for k in range(l):
			if k%2 == 0:
				res += res_index[k][::-1]
			else:
				res += res_index[k]
		return res
a = Solution()
print(a.findDiagonalOrder([
			 [ 1, 2, 3 ],
			 [ 4, 5, 6 ],
			 [ 7, 8, 9 ],
			]))


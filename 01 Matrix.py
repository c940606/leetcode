class Solution(object):
	def updateMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		print(matrix)
		row = len(matrix)
		col = len(matrix[0])

		def helper(i, j):
			# 上
			# up = 0
			temp_up = i-1
			while temp_up > 0 and matrix[temp_up ][j] != 0:
				temp_up -= 1
				# up += 1
			up = i - temp_up
			if temp_up == -1:
				up = 10000
			# 下
			# down = 0
			temp_down = i +1
			print(temp_down)
			while temp_down < row and matrix[temp_down ][j] != 0:
				temp_down += 1
				# down += 1
			down = temp_down - i
			if temp_down == row:
				down = 10000

			# 左
			# left = 0
			temp_left = j - 1
			while temp_left > 0 and matrix[i][temp_left] != 0:
				temp_left -= 1
				# left += 1
			left = j - temp_left
			if temp_left == -1:
				left = 10000

			# 右
			# right = 0
			temp_right = j + 1
			while temp_right < col and matrix[i][temp_right ] != 0:
				temp_right += 1
				# right += 1
			right = col - temp_right
			if temp_right == col:
				right = 10000
			print(up,down,left,right)
			return min(up, down, left, right)

		res = [[0] * col for _ in range(row)]
		for i in range(row):
			for j in range(col):
				if matrix[i][j] == 1:
					print(i,j)
					res[i][j] = helper(i, j)
		return res
a = Solution()
print(a.updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))
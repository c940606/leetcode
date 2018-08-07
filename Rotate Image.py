import math
class Solution:
	def rotate(self, matrix):
		"""
		给定一个 n × n 的二维矩阵表示一个图像。
		将图像顺时针旋转 90 度
		---
		给定 matrix =
				[
				  [1,2,3],
				  [4,5,6],
				  [7,8,9]
				],

				原地旋转输入矩阵，使其变为:
				[
				  [7,4,1],
				  [8,5,2],
				  [9,6,3]
				]
				给定 matrix =
					[
					  [ 5, 1, 9,11],
					  [ 2, 4, 8,10],
					  [13, 3, 6, 7],
					  [15,14,12,16]
					],

					原地旋转输入矩阵，使其变为:
					[
					  [15,13, 2, 5],
					  [14, 3, 4, 1],
					  [12, 6, 8, 9],
					  [16, 7,10,11]
					]
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		# 上下对调
		n = len(matrix)
		for i in range(n//2):
			matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
			print(matrix)
		#关于对角线对称
		for i in range(n):
			for j in range(i+1,n):
				matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
				print(matrix)



a = Solution()
matrix = [
		  [1,2,3],
		  [4,5,6],
		  [7,8,9]
		]
matrix1 =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
matrix3 = [[136,345,335,162,138,204,16,93,323,40,355,189,270,146,345,300,311,179,77],[70,223,267,9,125,125,211,304,231,166,148,231,303,133,206,45,212,51,2],[246,14,43,241,144,254,328,129,134,280,249,212,291,52,120,302,119,186,93],[63,57,260,153,289,203,227,136,249,20,128,192,267,83,236,89,228,130,57],[298,206,278,127,359,210,180,59,92,300,246,126,305,245,27,98,174,171,326],[251,1,287,19,194,195,43,11,285,272,82,283,150,289,142,278,289,293,99],[349,25,340,176,92,285,61,120,324,176,233,231,68,175,158,28,9,354,73],[21,219,286,105,83,77,335,226,356,204,159,35,194,125,16,311,218,242,12],[280,207,189,153,78,198,329,237,228,279,172,242,242,332,168,288,55,246,263],[282,243,108,21,219,243,147,176,194,6,59,147,287,207,337,20,226,176,350],[43,345,209,216,227,91,129,35,19,185,283,224,48,106,333,10,326,156,159],[143,351,106,143,78,334,351,55,355,157,172,285,201,157,134,58,325,167,128],[1,187,314,225,51,303,272,325,315,238,121,54,322,52,161,45,131,135,337],[128,70,134,241,296,337,39,70,336,305,178,104,307,6,359,172,359,303,84],[265,198,264,327,253,166,20,355,153,92,70,130,161,141,266,43,77,183,23],[88,99,329,268,144,217,215,143,330,154,26,356,59,225,200,27,58,6,349],[53,160,21,64,232,124,206,78,168,224,262,132,254,302,41,102,86,259,258],[230,170,52,198,166,53,3,6,81,63,314,10,57,55,333,63,288,97,270],[6,206,75,209,339,270,91,322,12,178,161,211,349,332,204,187,138,258,192]]
#[[3,1],[4,2]]
print(a.rotate(matrix))
print(a.rotate(matrix1))
print(a.rotate(matrix3))



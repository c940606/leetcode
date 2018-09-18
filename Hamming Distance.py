class Solution(object):
	def hammingDistance(self, x, y):
		"""
		两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
		给出两个整数 x 和 y，计算它们之间的汉明距离。
		---
		输入: x = 1, y = 4
		输出: 2
		解释:
		1   (0 0 0 1)
		4   (0 1 0 0)
			  ↑   ↑
		上面的箭头指出了对应二进制位不同的位置。
		---
		思路
		:type x: int
		:type y: int
		:rtype: int
		"""
		x_bin = bin(x)[2:]
		y_bin = bin(y)[2:]
		print(x_bin,y_bin)
		i = len(x_bin)
		j = len(y_bin)
		count = 0
		while i > 0 and j > 0:

			if x_bin[i-1] != y_bin[j-1]:
				count += 1
			i -= 1
			j -= 1
		print(i,j)
		print(count)
		if j > 0:
			temp = y_bin[:j].count("1")
			count += temp
		if i > 0:
			temp = x_bin[:i].count("1")
			count += temp

		return count
a = Solution()
print(a.hammingDistance(x = 1, y = 4))


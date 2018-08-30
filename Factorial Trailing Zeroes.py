import math


class Solution(object):
	def trailingZeroes(self, n):
		"""
		给定一个整数 n，返回 n! 结果尾数中零的数量。
		---
		输入: 3
		输出: 0
		解释: 3! = 6, 尾数中没有零。
		---
		输入: 5
		输出: 1
		解释: 5! = 120, 尾数中有 1 个零.
		---
		思路：
		用math 函数 factorial()求阶乘
		转化字符串
		看尾数有几个零
		:type n: int
		:rtype: int
		"""
		val = str(math.factorial(n))
		print(val)
		print(len(val))
		count = 0
		for num in val[::-1]:
			if num == "0":
				count += 1
			else:
				break
		return count

	def trailingZeroes1(self, n):
		self.res = []
		self.divfive(n)
		return sum(self.res)

	def divfive(self, n):
		val = n//5
		if val == 0:
			return
		self.res.append(val)
		self.divfive(val)


a = Solution()
print(a.trailingZeroes1(7268))

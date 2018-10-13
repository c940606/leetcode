class Solution(object):
	def addDigits1(self, num):
		"""
		给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
		----
		输入: 38
		输出: 2
		解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
		---
		思路:
		1.循环
		终止条件,位数为1
		2. 递归

		3.

		:type num: int
		:rtype: int
		"""
		while len(str(num))> 1:
			num = sum(map(int,str(num)))
		return num

	def addDigits2(self, num):
		res = []
		def helper(num):
			if len(str(num)) == 1:
				res.append(num)
				return
			helper(sum(map(int,str(num))))
		helper(num)
		return res[0]
a = Solution()
print(a.addDigits2(38))


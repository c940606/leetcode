class Solution(object):
	def maximumSwap(self, num):
		"""
		给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
		---
		输入: 2736
		输出: 7236
		解释: 交换数字2和数字7。
		---
		输入: 9973
		输出: 9973
		解释: 不需要交换。
		---
		思路：
		找到最大值，于首尾调换
		:type num: int
		:rtype: int
		"""
		num = list(map(int,str(num)))
		print(num)
		n = len(num)
		# flag = 1
		i = 0
		while i < n:
			max_val = max(num[i:])
			# print(max_val)
			if num[i] == max_val:
				i += 1
			else:
				index = num[i:].index(max_val)

				num[i],num[i+index] = num[i+index],num[i]
				break
		print(num)
		return int("".join(map(str,num)))
a = Solution()
print(a.maximumSwap(98368))

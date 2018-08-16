import math
class Solution(object):
	def countPrimeSetBits(self, L, R):
		"""
		给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。
		（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）
		---
		输入: L = 6, R = 10
		输出: 4
		解释:
		6 -> 110 (2 个计算置位，2 是质数)
		7 -> 111 (3 个计算置位，3 是质数)
		9 -> 1001 (2 个计算置位，2 是质数)
		10-> 1010 (2 个计算置位，2 是质数)
		---
		思路：
		首先把整数的转化二进制，在提取中1的个数,放入列表
		在从列表中看是不是质数
		:type L: int
		:type R: int
		:rtype: int
		"""
		one_num = []
		count = 0
		for num in range(L,R+1):
			one_num.append(bin(num).count("1"))
		for num in one_num:
			if self.is_prime(num):
				count += 1
		return count


	def is_prime(self,number):
		if number > 1:
			if number == 2:
				return True
			if number % 2 == 0:
				return False
			for current in range(3, int(math.sqrt(number) + 1), 2):
				if number % current == 0:
					return False
			return True
		return False
a = Solution()
print(a.countPrimeSetBits(6,10))

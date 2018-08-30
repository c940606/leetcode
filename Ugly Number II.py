class Solution(object):
	def nthUglyNumber(self, n):
		"""
		编写一个程序，找出第 n 个丑数。
		丑数就是只包含质因数 2, 3, 5 的正整数。
		--
		输入: n = 10
		输出: 12
		解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
		---
		思路：

		:type n: int
		:rtype: int
		"""
		res = [1]
		num_2 = 0
		num_3 = 0
		num_5 = 0
		while n > 1:
			res.append(min(res[num_2]*2,res[num_3]*3,res[num_5]*5))
			# print(res[-1])
			if res[-1] // res[num_2] == 2:
				num_2 += 1
			if res[-1] // res[num_3] == 3:
				num_3 += 1
			if res[-1] // res[num_5] == 5:
				num_5 += 1
			n -= 1
		return res[-1]
a = Solution()
print(a.nthUglyNumber(10))
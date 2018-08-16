class Solution(object):
	def monotoneIncreasingDigits(self, N):
		"""
		给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
		（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
		---
		输入: N = 10
		输出: 9
		---
		输入: N = 1234
		输出: 1234
		---
		输入: N = 332
		输出: 299
		---
		思路：
		从最小位比较
		如果 最低位 >=次地位:
		 	相应位置向前移动
		要不然，最高位-1 后面位数 全部变成9
		:type N: int
		:rtype: int
		"""
		N = list(map(int,str(N)))
		n = len(N)
		j = n-1
		i = n-2
		end = n
		while i>= 0 :
			if N[j] >= N[i]:
				pass
			else:
				# N[j] = 9
				N[i] -= 1
				# i 以后都是9
				for k in range(i+1,end):
					N[k] = 9
				end = i + 1
			i -= 1
			j -= 1
		# print(N)
		return int("".join(map(str,N)))
a = Solution()
print(a.monotoneIncreasingDigits(123456789))
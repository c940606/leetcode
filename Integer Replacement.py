class Solution(object):
	def integerReplacement(self, n):
		"""
		给定一个正整数 n，你可以做如下操作：
			1. 如果 n 是偶数，则用 n / 2替换 n。
			2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
			n 变为 1 所需的最小替换次数是多少？
		---
		输入:
		8
		输出:
		3
		解释:
		8 -> 4 -> 2 -> 1
		---
		输入:
		7
		输出:
		4
		解释:
		7 -> 8 -> 4 -> 2 -> 1
		或
		7 -> 6 -> 3 -> 2 -> 1
		---
		思路：
		自取n-1
		:type n: int
		:rtype: int
		"""
		# count = 0
		# while n != 1:
		# 	print(n,"--->",end="")
		# 	if n%2==0:
		# 		n /=2
		# 	else:
		# 		n -= 1
		# 	count += 1
		# return count
		if n%2 == 0:
			return 1
		
a = Solution()
print(a.integerReplacement(65535))

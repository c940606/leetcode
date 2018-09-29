class Solution(object):
	def largestPalindrome(self, n):
		"""
		你需要找到由两个 n 位数的乘积组成的最大回文数。
		由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。
		示例:
		输入: 2
		输出: 987
		解释: 99 x 91 = 9009, 9009 % 1337 = 987
		说明:
		n 的取值范围为 [1,8]
		--

		:type n: int
		:rtype: int
		"""
		num = 10**n-1
		A = num
		B = num
		while A>=1:
			print(A,B)
			temp_num = A*B
			temp = str(temp_num)
			if temp == temp[::-1]:
				print("1",A,B,temp)
				return temp_num%1337
			B -= 1
			print(A,B)
			temp_num = A * B
			temp = str(temp_num)
			if temp == temp[::-1]:
				print("1", A, B, temp)
				return temp_num % 1337
			A = B

a = Solution()
print(a.largestPalindrome(3))


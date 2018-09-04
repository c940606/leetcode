class Solution:
	# @param n, an integer
	# @return an integer
	#颠倒给定的 32 位无符号整数的二进制位。
	def reverseBits(self, n):
		# print(bin(n))
		s = bin(n)[2:]
		print(s)


		s = s[::-1]
		print((s))
		s += "0" * (32 - len(s))
		print(s)
		return int(s,2)
a = Solution()
print(a.reverseBits(43261596))
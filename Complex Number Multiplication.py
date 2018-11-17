class Solution(object):
	def complexNumberMultiply(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		a = a.split("+")
		b = b.split("+")
		# print(a,b)
		# 实数
		c1 = int(a[0])*int(b[0])
		# print("c1:",c1)
		# 实 和 虚
		# print(b[1][:-1])
		c2 = int(a[0])*int(b[1][:-1])
		c3 = int(b[0])* int(a[1][:-1])
		# xu
		c4 = (-1)*int(b[1][:-1])*int(a[1][:-1])
		return str(c1+c4)+"+"+str(c2+c3)+"i"
a = Solution()
print(a.complexNumberMultiply("1+1i", "1+1i"))
print(a.complexNumberMultiply("1+-1i", "1+-1i"))
class Solution(object):
	def toHex(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if  num == 0:
			return "0"
		lookup = "0123456789abcdef"
		res = ""
		for i in range(8):
			n = num & 15
			print(n)
			res = lookup[n] + res
			num = num >> 4
			if num == 0:
				break
		return res
a = Solution()
print(a.toHex(-1))
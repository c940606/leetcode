class Solution(object):
	def findComplement(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		bin_num = bin(num)[2:]
		s = ""
		n = len(bin_num)
		i = 0
		while i <n:
			if bin_num[i] == "0":
				s += "1"
			elif bin_num[i] == "1":
				s += "0"
			i += 1
		print(s)
		return int(s,2)
a = Solution()
print(a.findComplement(5))
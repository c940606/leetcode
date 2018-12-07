


class Solution(object):
	def originalDigits(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		from collections import defaultdict
		from collections import Counter
		if not s:
			return ""
		# c = Counter(s)
		letter = ['z', 'w', 'u', 'x', 'g', 'o', 'h', 'f', 'v', 'i', "s"]
		c = {x: s.count(x) for x in letter}
		res = defaultdict(int)
		res[0] = c["z"]
		res[2] = c["w"]
		res[6] = c["x"]
		res[7] = c["s"]
		res[8] = c["g"]
		res[4] = c["u"]
		res[5] = c["f"]
		res[3] = c["h"]
		res[9] = c["i"]
		res[1] = c["o"]
		# for alp in s:
		# 	# 0
		# 	if alp == "z":
		# 		res[0] += 1
		# 	# 2
		# 	if alp == "w":
		# 		res[2] += 1
		# 	# 6
		# 	if alp == "x":
		# 		res[6] += 1
		# 	# 6 7
		# 	if alp == "s":
		# 		res[7] += 1
		# 	# 8
		# 	if alp == "g":
		# 		res[8] += 1
		# 	# 4
		# 	if alp == "u":
		# 		res[4] += 1
		# 	# 4 5
		# 	if alp == "f":
		# 		res[5] += 1
		# 	# 3 8
		# 	if alp == "h":
		# 		res[3] += 1
		# 	# 9 8 5 6
		# 	if alp == "i":
		# 		res[9] += 1
		# 	# 1 0 2 4
		# 	if alp == "o":
		# 		res[1] += 1
		print(res)
		res[7] -= res[6]
		res[5] -= res[4]
		res[3] -= res[8]
		res[9] -= (res[8] + res[5] + res[6])
		res[1] -= (res[0] + res[2] + res[4])
		print(res)
		ret = ""
		for i in range(0,10):
			ret += str(i) * res[i]
		return ret


a = Solution()
print(a.originalDigits("owoztneoer"))
print(a.originalDigits("fviefuro"))

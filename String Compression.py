class Solution(object):
	def compress(self, chars):
		"""
		:type chars: List[str]
		:rtype: int
		"""
		if not chars:
			return 0
		n = len(chars)
		i = 0
		res = []
		while i < n:
			num = 1
			while i < n-1 and chars[i] == chars[i+1]:
				i += 1
				num += 1
			if num == 1:
				res.append(chars[i])
			else:
				res.append(chars[i])
				res.extend(list(str(num)))
			print(res)
			i += 1
		# print(res)
		return len(res)
a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))
print(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(a.compress(["a"]))
print(a.compress(["a","a","b","b","c","c","c"]))
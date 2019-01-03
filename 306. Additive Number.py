class Solution:
	def isAdditiveNumber(self, num):
		"""
		:type num: str
		:rtype: bool
		"""
		if not num:
			return False
		res = []
		n = len(num)

		def helper(idx):
			if idx == n and len(res) > 2:
				return True
			for i in range(idx, n):
				if num[idx] == "0" and i > idx:
					break
				tmp = int(num[idx:i + 1])
				tmp_n = len(res)
				if tmp_n >=2 and tmp > res[-1] +res[-2]:
					break
				if tmp_n <= 1 or tmp == res[-1] + res[-2]:
					res.append(tmp)
					if helper(i + 1):
						return True
					res.pop()
			return False

		return helper(0)

a = Solution()
print(a.isAdditiveNumber("112358"))
print(a.isAdditiveNumber("199100199"))

class Solution:
	def splitIntoFibonacci(self, S):
		"""
		:type S: str
		:rtype: List[int]
		"""
		if not S:
			return []
		res = []
		n = len(S)

		def helper(S, res, idx):
			# 终止条件,说明遍历整个字符串
			if idx == n and len(res) >= 3:
				return True

			for i in range(idx, n):
				# 当开头为"0"并且不止一位数的时候
				if S[idx] == "0" and i > idx:
					break

				num = int(S[idx:i + 1])
				tmp_n = len(res)
				# 不能超过最大整数
				if num > 2147483647:
					break
				# 前面两个数之和大于现在这个数
				if tmp_n >= 2 and num > res[-1] + res[-2]:
					break
				if tmp_n <= 1 or num == res[-1] + res[-2]:
					res.append(num)
					if helper(S, res, i + 1):
						return True
					res.pop()
			return False

		helper(S, res, 0)
		return res


a = Solution()
print(a.splitIntoFibonacci("123456579"))
print(a.splitIntoFibonacci("11235813"))
print(a.splitIntoFibonacci("112358130"))
print(
	a.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))

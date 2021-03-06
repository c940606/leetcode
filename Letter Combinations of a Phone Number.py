
class Solution:
	def letterCombinations(self, digits):
		"""
		给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
		给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
		--------------------------
		输入："23"
		输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
		:type digits: str
		:rtype: List[str]
		"""
		if digits == "":
			return []
		self.lookup = {
			1:"",
			2:"abc",
			3:"def",
			4:"ghi",
			5:"jkl",
			6:"mno",
			7:"pqrs",
			8:"tuv",
			9:"wxyz"
		}
		digits = list(map(int,digits))
		self.res = []
		self.singleResult("",digits)
		return self.res

	def singleResult(self, s, digits):
			if len(digits) == 0:
				self.res.append(s)
			else:
				for i in self.lookup[digits[0]]:
					self.singleResult(s+i,digits[1:])

	def letterCombinations1(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		lookup = {
			1: "",
			2: "abc",
			3: "def",
			4: "ghi",
			5: "jkl",
			6: "mno",
			7: "pqrs",
			8: "tuv",
			9: "wxyz"
		}
		if not digits:
			return []
		res = []
		n = len(digits)

		def helper(digits, n, s):
			if n == 0:
				res.append(s)
				return
			for i in (lookup[int(digits[0])]):
				helper(digits[1:], n - 1, s + i)

		helper(digits, n, "")
		return res


a = Solution()
print(a.letterCombinations("64434523"))
print(a.letterCombinations1("64434523"))
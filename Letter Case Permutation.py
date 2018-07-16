class Solution:
	def letterCasePermutation(self, S):
		"""
		给定一个字符串S，通过将字符串S中的每个字母转变大小写，
		我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
		---------
		示例:
			输入: S = "a1b2"
			输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

			输入: S = "3z4"
			输出: ["3z4", "3Z4"]

			输入: S = "12345"
			输出: ["12345"]
		:type S: str
		:rtype: List[str]
		"""

		self.res = []
		self.dft("",0,S)
		return self.res
	def dft(self,s,index,S):
		if index == len(S) and s not in self.res:
			self.res.append(s)
		if index < len(S):
			temp = [S[index]]
			if S[index].upper() not in temp:
				temp += [S[index].upper()]
			elif S[index].lower() not in temp:
				temp += [S[index].lower()]
			for i in temp:
				self.dft(s+i,index+1,S)
S1 = "a1b2dsaf"
S2= "3z4"
S3 = "12345a"
a = Solution()
print(a.letterCasePermutation(S1))
print(a.letterCasePermutation(S2))
print(a.letterCasePermutation(S3))
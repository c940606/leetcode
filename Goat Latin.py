class Solution(object):
	def toGoatLatin(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		if not S:
			return ""
		S = S.split(" ")
		res = []

		def helper(idx,word):
			lookup = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
			if word[0] in lookup:
				return word+"ma"+"a"*(idx+1)
			else:
				return word[1:]+word[0]+"ma"+"a"*(idx+1)

		for idx,word in enumerate(S):
			temp = helper(idx,word)
			res.append(temp)
		return " ".join(res)
a = Solution()
print(a.toGoatLatin("I speak Goat Latin"))
print(a.toGoatLatin("The quick brown fox jumped over the lazy dog"))
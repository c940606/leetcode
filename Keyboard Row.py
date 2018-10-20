class Solution(object):
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		flag = [{"q","w","e","r","t","y","u","i","o","p"},{"a","s","d","f","g","h","j","k","l"},{"z","x","c","v","b","n","m"}]
		res = []
		for word in words:
			temp = set(word.lower())
			# print(temp)
			for item in flag:
				if temp.issubset(item):
					res.append(word)
		return res
a = Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))
class Solution(object):
	def isAlienSorted(self, words, order):
		"""
		:type words: List[str]
		:type order: str
		:rtype: bool
		"""
		lookup = {}
		for idx, alp in enumerate(order):
			lookup[alp] = idx
		words = [[lookup[c] for c in w] for w in words]
		return sorted(words) == words


a = Solution()
print(a.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
# print(a.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
# print(a.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
# print(a.isAlienSorted(["kuvp","q"],"ngxlkthsjuoqcpavbfdermiywz"))
print(a.isAlienSorted(["iekm", "tpnhnbe"], "loxbzapnmstkhijfcuqdewyvrg"))

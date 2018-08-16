class Solution(object):
	def uniqueMorseRepresentations(self, words):
		"""
		国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串，
		比如: "a" 对应 ".-", "b" 对应 "-...", "c" 对应 "-.-.", 等等。
		为了方便，所有26个英文字母对应摩尔斯密码表如下：
		[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，"cab" 可以写成 "-.-.-....-"，
		(即 "-.-." + "-..." + ".-"字符串的结合)。我们将这样一个连接过程称作单词翻译。
		返回我们可以获得所有词不同单词翻译的数量。
		----
		例如:
			输入: words = ["gin", "zen", "gig", "msg"]
			输出: 2
			解释:
			各单词翻译如下:
			"gin" -> "--...-."
			"zen" -> "--...-."
			"gig" -> "--...--."
			"msg" -> "--...--."

			共有 2 种不同翻译, "--...-." 和 "--...--.".
		---
		思路：
		把每个单词解码，放入列表里，用集合取长度
		:type words: List[str]
		:rtype: int
		"""
		self.lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		# print(len(self.lookup))
		self.res = []
		for word in words:
			self.transformation(word)
		print(self.res)
		return len(set(self.res))

	def transformation(self, word):
		# print(word)
		s = ""
		for alp in word:
			# print(alp)
			# print(s)
			s += self.lookup[ord(alp.lower())-97]
		self.res.append(s)
		# return
a = Solution()
print(a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
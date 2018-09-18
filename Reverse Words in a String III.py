class Solution(object):
	def reverseWords(self, s):
		"""
		给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
		----
		输入: "Let's take LeetCode contest"
		输出: "s'teL ekat edoCteeL tsetnoc"
		:type s: str
		:rtype: str
		"""
		return " ".join(map(lambda x:x[::-1],s.split()))
a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))
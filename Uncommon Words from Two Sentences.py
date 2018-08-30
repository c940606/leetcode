from collections import Counter


class Solution(object):
	def uncommonFromSentences(self, A, B):
		"""
		给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
		如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
		返回所有不常用单词的列表。
		您可以按任何顺序返回列表。
		---
		思路：
		用 字典
		:type A: str
		:type B: str
		:rtype: List[str]
		"""
		new_string = A +" "+ B
		new_string = new_string.split(" ")
		# print(new_string)
		c = Counter(new_string)
		res = []
		for item in c.items():
			if item[1] == 1:
				res.append(item[0])
		return res
a = Solution()
A = "this apple is sweet"
B = "this apple is sour"
print(a.uncommonFromSentences(A,B))


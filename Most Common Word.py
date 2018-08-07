from collections import Counter


class Solution:
	def mostCommonWord(self, paragraph, banned):
		"""
		给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，
		同时不在禁用列表中的单词。题目保证至少有一个词不在禁用列表中，而且答案唯一。
		禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
		---
		输入:
		paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
		banned = ["hit"]
		输出: "ball"
		"!?',;."
		---
		思路:
		1. 把所有单词分割出来
		2. 统计单词个数
		3. 从多到少找不在禁止区的单词
		4. 输出
		:type paragraph: str
		:type banned: List[str]
		:rtype: str
		"""
		count_word = Counter(self.split_word(paragraph))
		count_word	 = sorted(count_word.items(),key=lambda x:x[1],reverse=True)
		print(count_word)
		for key in  count_word:
			if key[0] not in banned:
				return key[0]
	def split_word(self,paragraph):
		split_word_list = paragraph.split()
		for i in range(len(split_word_list)):
			if split_word_list[i][-1] in "!?',;.":
				split_word_list[i] = split_word_list[i][:-1]
			split_word_list[i] = split_word_list[i].lower()
		return split_word_list
a = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))



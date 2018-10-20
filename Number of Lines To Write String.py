class Solution(object):
	def numberOfLines(self, widths, S):
		"""
		我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，
		如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。
		我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位，
		widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。
		现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
		----

		:type widths: List[int]
		:type S: str
		:rtype: List[int]
		"""
		if not S:
			return []
		n = len(S)
		i = 0
		row_count = 0
		while i < n:
			row_num = 0
			while i < n and row_num+widths[ord(S[i])-97] <= 100:
				row_num += widths[ord(S[i])-97]
				i += 1
			row_count += 1
		return [row_count,row_num]
a = Solution()
print(a.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"))
print(a.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))

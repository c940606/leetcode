class Solution(object):
	def largeGroupPositions(self, S):
		"""
		在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。
		例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
		我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。
		最终结果按照字典顺序输出。
		---
		输入: "abbxxxxzzy"
		输出: [[3,6]]
		解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。
		---
		输入: "abc"
		输出: []
		解释: "a","b" 和 "c" 均不是符合要求的较大分组。
		---
		输入: "abcdddeeeeaabbbcd"
		输出: [[3,5],[6,9],[12,14]]
		:type S: str
		:rtype: List[List[int]]
		"""
		if not S:
			return []
		n = len(S)
		i = 0
		res = []
		while i < n:
			# print(i)
			beg = i
			while i < n-1 and S[i] == S[i+1]:
				i += 1
			last = i
			if last - beg >= 2:
				res.append([beg,last])
			i += 1
		return res
a = Solution()
print(a.largeGroupPositions("abc"))

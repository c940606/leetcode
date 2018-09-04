from collections import Counter


class Solution(object):
	def frequencySort(self, s):
		"""
		给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
		----
		输入:
		"tree"
		输出:
		"eert"
		解释:
		'e'出现两次，'r'和't'都只出现一次。
		因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
		---
		1. collections
		2. 字典排序
		3. 组成字符串
		:type s: str
		:rtype: str
		"""
		c = Counter(s)
		c  =sorted(c.items(),key= lambda x:x[1],reverse=True)
		s = ""
		for item in c:
			s += item[0]*item[1]
		return s
a = Solution()
print(a.frequencySort("tree"))
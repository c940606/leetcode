class Solution:
	def groupAnagrams(self, strs):
		"""
		给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
		----
		输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
		输出:
		[
		  ["ate","eat","tea"],
		  ["nat","tan"],
		  ["bat"]
		]
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		lookup = {}
		# print(strs)
		for item in strs:
			# print(item)
			temp = "".join(sorted(item))
			if temp in lookup:
				lookup[temp] += [item]
			else:
				lookup[temp] = [item]
		return list(lookup.values())
a = Solution()
str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(a.groupAnagrams(str1))
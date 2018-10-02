from collections import Counter


class Solution(object):
	def wordSubsets(self, A, B):
		"""
		:type A: List[str]
		:type B: List[str]
		:rtype: List[str]
		"""
		if not A or not B:
			return []
		s = "".join(B)
		s = set(s)
		print(s)
		# count_s = Counter(s)
		# key_list = list(count_s.keys())
		count_s = {}
		for i in s:
			count_s[i] = 0
		print(count_s)
		for i in s:
			for string in B:
				if i in string and string.count(i)>count_s[i]:
					count_s[i] = string.count(i)
		print(count_s)

		n = len(A)
		res = []
		for i in range(n):
			if all(map(lambda key : True if A[i].count(key)>=count_s[key] else False,count_s.keys())):
				res.append(A[i])
			# for key in count_s.keys():
			# 	if A[i].count(key) < count_s[key]:
			# 		break
			# res.append(A[i])
		return res
a = Solution()
print(a.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]))

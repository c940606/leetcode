class Solution(object):
	def numMatchingSubseq(self, S, words):
		"""
		:type S: str
		:type words: List[str]
		:rtype: int
		"""
		from collections import Counter
		count = 0
		words = Counter(words)
		for word,num in words.items():
			tmp = S
			flag = False
			for alp in word:
				idx = tmp.find(alp)
				if idx == -1:
					flag = True
					break
				else:
					tmp = tmp[idx + 1:]
			if not flag:
				count += num
		return count

	def numMatchingSubseq1(self, S, words):
		from collections import defaultdict,Counter

		import bisect
		def isMatch(word, w_i, d_i):
			if w_i == len(word): return True
			l = dict_idxs[word[w_i]]
			if len(l) == 0 or d_i > l[-1]: return False
			i = l[bisect.bisect_left(l, d_i)]

			# i = l[l.index(d_i)]
			# print(i)
			return isMatch(word, w_i + 1, i + 1)

		dict_idxs = defaultdict(list)
		print(Counter(words))
		for i in range(len(S)):
			dict_idxs[S[i]].append(i)
		return sum(isMatch(word, 0, 0) for word in words)


a = Solution()
print(a.numMatchingSubseq1(S="abcde", words=["a", "bb", "acd", "ace"]))

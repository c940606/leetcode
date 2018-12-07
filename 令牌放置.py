class Solution(object):
	def bagOfTokensScore(self, tokens, P):
		"""
		:type tokens: List[int]
		:type P: int
		:rtype: int
		"""
		if not tokens:
			return 0
		res = 0
		tokens.sort()
		if tokens[0] > P:
			return 0
		P += tokens[0]
		for token in tokens:
			if P >= token:
				res += 1
				P -= token
			else:
				P += token
				res -= 1
		return res

	def bagOfTokensScore1(self, tokens, P):
		tokens.sort()
		j = len(tokens) - 1
		i = 0
		res = 0
		cur = 0
		while i <= j:
			if P >=  tokens[i]:
				print("加分",tokens[i])
				cur += 1
				P -= tokens[i]
				res = max(res,cur)
				print(res)
				i += 1
			elif cur > 0:
				print("减分",tokens[j])
				P += tokens[j]
				j -= 1
				cur -= 1
			else:
				break
		return res

a = Solution()
print(a.bagOfTokensScore1(tokens=[100, 200, 300, 400], P=200))
print(a.bagOfTokensScore1(tokens=[100, 200], P=150))
print(a.bagOfTokensScore1([58, 91], 50))


class Solution:
	def predictPartyVictory(self, senate):
		"""
		:type senate: str
		:rtype: str
		"""
		from collections import deque
		R = deque()
		D = deque()
		n = len(senate)
		for idx, alp in enumerate(senate):
			if alp == "R":
				R.appendleft(idx)
			else:
				D.appendleft(idx)
		# print(R)
		# print(D)
		while R and D:
			idx_R = R.pop()
			idx_D = D.pop()
			if idx_R < idx_D:
				R.appendleft(idx_R + n)
			else:
				D.appendleft(idx_D + n)
		return "Radiant" if len(R) > len(D) else "Dire"


a = Solution()
print(a.predictPartyVictory("RD"))
print(a.predictPartyVictory("RDD"))

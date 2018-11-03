class Solution(object):
	def minFlipsMonoIncr(self, S):
		"""
		:type S: str
		:rtype: int
		"""
		front_zero = [0]
		last_one = [0]
		n = len(S)
		for i in range(n):
			if S[i] == "0":
				front_zero.append(front_zero[-1])
			else:
				front_zero.append(front_zero[-1]+1)
		temp_S = S[::-1]
		for i in range(n):
			if temp_S[i] == "1":
				last_one.append(last_one[-1])
			else:
				last_one.append(last_one[-1]+1)
		last_one = last_one[::-1]
		max_t= 200001
		for x,y in zip(front_zero,last_one):
			if x + y < max_t:
				max_t = x + y
		return max_t
a = Solution()
print(a.minFlipsMonoIncr("00110"))

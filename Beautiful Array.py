class Solution(object):
	def beautifulArray(self, N):
		"""
		:type N: int
		:rtype: List[int]
		"""
		res = [1]
		while len(res) < N:
			res = [i * 2 -1 for i in res] + [i * 2 for i in res]
			# print(res)
		return [i for i in res if i <= N]

	def beautifulArray1(self, N):
		if N == 1: return [1]
		odd = [i * 2 - 1 for i in self.beautifulArray1((N+1)//2)]
		# print("odd",odd)
		even = [i * 2 for i in self.beautifulArray1(N//2)]
		# print("even",even)
		return odd + even



a = Solution()
print(a.beautifulArray1(5))

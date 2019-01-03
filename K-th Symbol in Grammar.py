class Solution:
	def kthGrammar(self, N, K):
		"""
		:type N: int
		:type K: int
		:rtype: int
		"""
		self.res = ""
		def helper2(param):
			res = ""
			for alp in param:
				if alp == "0":
					res += "1"
				else:
					res += "0"
			return res
		def helper1(N,param):
			if N == 1:
				self.res = param
				return
			# print(param)
			helper1(N-1,param + helper2(param))
		helper1(N,"0")
		# print(self.res)
		return self.res[K-1]


a = Solution()
print(a.kthGrammar(4,5))
print(a.kthGrammar(30,434991989))

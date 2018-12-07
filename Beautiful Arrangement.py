class Solution(object):
	def countArrangement(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		if N == 0:return 0
		self.count = 0
		def helper(N,pos,used):
			if pos > N:
				self.count += 1
				return
			for i in range(1,N+1):
				if used[i] == 0 and (i % pos == 0 or pos % i == 0):
					used[i] = 1
					helper(N,pos+1,used)
					used[i] = 0

		helper(N,1,[0]*(N+1))
		return self.count
a = Solution()
print(a.countArrangement(5))
class Solution(object):
	def knightDialer(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		lookup = {
			1:[6,8],
			2:[7,9],
			3:[4,8],
			4:[3,9,0],
			5:[],
			6:[1,7,0],
			7:[2,6],
			8:[1,3],
			9:[2,4],
			0:[4,6]
		}
		if N == 0:
			return 0
		if N == 1:
			return 10
		self.res = 0
		def helper(loc,count):
			if count==0:
				self.res += 1
				return
			for num in lookup[loc]:
				helper(num,count-1)
		for i in range(10):
			helper(i,N-1)
		return self.res%(10**9+7)

	def knightDialer1(self, N):
		lookup = {
			1: [6, 8],
			2: [7, 9],
			3: [4, 8],
			4: [3, 9, 0],
			5: [],
			6: [1, 7, 0],
			7: [2, 6],
			8: [1, 3],
			9: [2, 4],
			0: [4, 6]
		}
		mod = 1000000007
		if N == 0:
			return 0
		if N == 1:
			return 10
		N -= 1
		dp = [1]*10
		for i in range(N):
			temp = [0]*10
			temp[1] = dp[6]+dp[8]
			temp[2] = dp[7]+dp[9]
			temp[3] = dp[4]+dp[8]
			temp[4] = dp[3]+dp[9]+dp[0]
			temp[6] = dp[1]+dp[7]+dp[0]
			temp[7] = dp[2]+dp[6]
			temp[8] = dp[1]+dp[3]
			temp[9] = dp[2]+dp[4]
			temp[0] = dp[4]+dp[6]
			dp = temp
		return sum(dp)%mod


a = Solution()
print(a.knightDialer(2))

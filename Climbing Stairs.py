class Solution:
	def climbStairs(self, n):
		"""
		假设你正在爬楼梯。需要 n 步你才能到达楼顶。
		每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
		注意：给定 n 是一个正整数。
		:type n: int
		:rtype: int
		"""
		stairs = [0]*(n+1)
		if n < 3:
			return n
		stairs[0] = 0
		stairs[1] = 1
		stairs[2] = 2
		for i in range(3,n+1):
			stairs[i] = stairs[i-1]+stairs[i-2]
		return stairs[n]
a = Solution()
print(a.climbStairs(4))
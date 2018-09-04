class Solution(object):
	def coinChange(self, coins, amount):
		"""
		给定不同面额的硬币 coins 和一个总金额 amount。
		编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
		---
		输入: coins = [1, 2, 5], amount = 11
		输出: 3
		解释: 11 = 5 + 5 + 1
		---
		输入: coins = [2], amount = 3
		输出: -1
		---
		思路:
		简单来说:就是需要0,1,2,3,4 需要多少个 硬币
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		dp = [-1]*(amount+1)
		i = 1
		while i < amount+1:
			if i in coins:
				dp[i] = [i]
				i += 1
				continue
			# print(i)
			temp = []
			# 判断前面有几个可以凑成来
			for j in range(i):
				# print(j)
				# print(dp[j])
				if dp[j] != -1:
					# print("这里",dp[j])
					target = i - sum(dp[j])
					# print("target",target)
					if target in coins:
						temp.append(dp[j]+[target])
			# print(temp)
			if not temp:
				dp[i] = -1
			else:
				dp[i] = self.min_list(temp)
			i += 1
			print(dp)
		if dp[-1] == -1:
			return 0
		return len(dp[-1])

	def min_list(self,ilist):
		min_len = 100000
		min_list = []
		for item in ilist:
			temp_len = len(item)
			if min_len  > temp_len:
				min_len = temp_len
				min_list = item
		return min_list





a = Solution()
print(a.coinChange(coins = [186,419,83,408], amount = 6249))
# print(a.min_list([[2, 2], [2, 1, 1]]))
# [186,419,83,408]
# 6249




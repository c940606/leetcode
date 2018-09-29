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

	def coinChange1(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		coins = sorted(coins, reverse=True)
		print(coins)
		count = 0
		while True:
			for coin in coins:
				print(amount,count)
				while amount - coin >= 0:
					count += 1
					amount -= coin
				if amount == 0:
					return count
			return -1

	def coinChange3(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		if coins == []:
			return -1
		if amount == 0:
			return 0
		dp = [0] * (amount + 1)

		for i in range(1, amount + 1):
			min_count = amount * 10
			for coin in coins:

				if i - coin >= 0 and min_count >= dp[i - coin] + 1:
					min_count = dp[i - coin] + 1
			dp[i] = min_count
		if dp[-1] == amount * 10:
			return -1
		return dp[-1]

	def coinChange2(self, coins, amount):
		if amount == 0:
			return 0
		if coins == []:
			return -1
		coins.sort()
		dp = [0] * (amount + 1)
		for i in range(1,amount+1):
			min_num = 0
			for coin in coins:
				if i == coin:
					dp[i] = 1
					continue
				print(dp)
				print(i)

				if i-coin> 0 and dp[i-coin] < min_num:
					min_num =
				dp[i] = min_num
		print(dp)
		if dp[-1]==0:
			return -1
		return dp[-1]




a = Solution()
print(a.coinChange2(coins = [186,419,83,408], amount = 6249))
print(a.coinChange2(coins = [2], amount = 1))
print(a.coinChange2([1,2147483647],2))
# print(a.min_list([[2, 2], [2, 1, 1]]))
# [186,419,83,408]
# 6249




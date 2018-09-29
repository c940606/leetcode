class Solution(object):
	def change(self, amount, coins):
		"""
		给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
		注意: 你可以假设
		0 <= amount (总金额) <= 5000
		1 <= coin (硬币面额) <= 5000
		硬币种类不超过500种
		结果符合32位符号整数
		---
		输入: amount = 5, coins = [1, 2, 5]
		输出: 4
		解释: 有四种方式可以凑成总金额:
		5=5
		5=2+2+1
		5=2+1+1+1
		5=1+1+1+1+1
		---
		输入: amount = 3, coins = [2]
		输出: 0
		解释: 只用面额2的硬币不能凑成总金额3。
		---
		输入: amount = 10, coins = [10]
		输出: 1
		--
		思路:
		递归
		:type amount: int
		:type coins: List[int]
		:rtype: int
		"""
		# res = []
		self.count = 0
		coins.sort()
		def helper(amount,temp):
			if amount == 0 :
				print(temp)
				self.count += 1
				# res.append((temp))
				return
			if amount < 0 :
				return
			for coin in coins:
				if  temp and temp[-1]>coin:
					continue
				helper(amount-coin,temp+[coin])
		helper(amount,[])
		# print(res)
		return self.count




a = Solution()
print(a.change1(amount = 5, coins = [1, 2, 5]))
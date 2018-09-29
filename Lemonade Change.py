class Solution(object):
	def lemonadeChange(self, bills):
		"""
		在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
		顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
		每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
		注意，一开始你手头没有任何零钱。
		如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
		---
		输入：[5,5,5,10,20]
		输出：true
		解释：
		前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
		第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
		第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
		由于所有客户都得到了正确的找零，所以我们输出 true。
		--
		字典
		:type bills: List[int]
		:rtype: bool
		"""
		if not bills:
			return True
		lookup = {
			5:0,
			10:0,
			20:0
		}
		n = len(bills)
		i = 0
		while i < n:
			if bills[i] == 5:
				lookup[5] += 1
			elif bills[i] == 10:
				if lookup[5] != 0:
					lookup[5] -= 1
					lookup[10] += 1
				else:
					return False
			elif bills[i] == 20:
				if (lookup[10]!=0 and lookup[5]!=0):
					lookup[10] -= 1
					lookup[5] -= 1
					lookup[20] += 1
				elif lookup[5] > 2:
					lookup[5] -= 3
					lookup[20] += 1
				else:
					return False
			i += 1
		print(lookup)
		return True
a = Solution()
print(a.lemonadeChange([5,5,5,10,20]))


class Solution(object):
	def minCostClimbingStairs(self, cost):
		"""
		数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
		每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
		您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
		--
		输入: cost = [10, 15, 20]
		输出: 15
		解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
		--
		输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
		输出: 6
		解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
		:type cost: List[int]
		:rtype: int
		"""
		n = len(cost)
		if n == 2:
			return min(cost[0],cost[1])
		res = [0]*(n+1)
		for i in range(2,n+1):
			res[i] = min(res[i-2]+cost[i-2],res[i-1]+cost[i-1])
			# print(res)
		return res[n]

a = Solution()
print(a.minCostClimbingStairs(cost = [10, 15, 20]))
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(a.minCostClimbingStairs([0,1,2,2]))
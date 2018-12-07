class Solution(object):
	def shoppingOffers(self, price, special, needs):
		"""
		在LeetCode商店中， 有许多在售的物品。
		然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
		现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。
		每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。
		任意大礼包可无限次购买。
		---
		输入: [2,5], [[3,0,5],[1,2,10]], [3,2]
		输出: 14
		解释:
		有A和B两种物品，价格分别为¥2和¥5。
		大礼包1，你可以以¥5的价格购买3A和0B。
		大礼包2， 你可以以¥10的价格购买1A和2B。
		你需要购买3个A和2个B， 所以你付了¥10购买了1A和2B（大礼包2），以及¥4购买2A。
		:type price: List[int]
		:type special: List[List[int]]
		:type needs: List[int]
		:rtype: int
		"""
		# self.res = float("inf")
		n = len(needs)
		def helper(special, needs):
			val = 0
			for i in range(n):
				val += needs[i] * price[i]
			for product in special:
				if all(map(lambda i :  True if needs[i]>=product[i] else False,range(n))):
					tmp = product[-1] + helper(special, list(map(lambda i:needs[i]-product[i],range(n))))
					val = min(val, tmp)

			return val
		return helper(special,needs)



a = Solution()
print(a.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]))
print(a.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
print(a.shoppingOffers([1,1,1],[[1,1,1,0],[2,2,1,1]],[1,1,0]))
print(a.shoppingOffers([9,9],[[1,1,1]],[2,2]))

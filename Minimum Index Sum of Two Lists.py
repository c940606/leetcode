class Solution(object):
	def findRestaurant(self, list1, list2):
		"""
		假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
		你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。
		如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
		---
		输入:
		["Shogun", "Tapioca Express", "Burger King", "KFC"]
		["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
		输出: ["Shogun"]
		解释: 他们唯一共同喜爱的餐厅是“Shogun”。
		---
		思路：
		找出共同喜欢的
		:type list1: List[str]
		:type list2: List[str]
		:rtype: List[str]
		"""
		common_like = set(list1) & set(list2)
		res = []
		min_index  = 2000
		for item in common_like:
			index1 = list1.index(item)
			index2 = list2.index(item)
			all_index = index1 + index2
			if min_index > all_index:
				min_index = all_index
				res.clear()
				res.append(item)
			elif min_index == all_index:
				res.append(item)
		return res
a = Solution()
print(a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))



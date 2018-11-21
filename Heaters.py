class Solution(object):
	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
		houses.sort()
		heaters.sort()
		heaters = [float("-inf")] + heaters + [float("inf")]
		max_val = 0
		i = 0
		for house in houses:
			while house > heaters[i+1]:
				i += 1
			print(i)
			print("---")
			temp = min(house-heaters[i],heaters[i+1]-house)
			max_val = max(max_val,temp)
		return max_val
a = Solution()
print(a.findRadius([1,2,3,4],[1,4]))
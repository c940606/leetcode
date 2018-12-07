class Solution(object):
	def findPoisonedDuration(self, timeSeries, duration):
		"""
		:type timeSeries: List[int]
		:type duration: int
		:rtype: int
		"""
		# n = len(timeSeries)
		# res = duration * n
		# for i in range(1,n):
		#     res -= max(0,duration - (timeSeries[ i ] - timeSeries[ i - 1 ]))
		# return res
		end = 0
		res = 0
		for t in timeSeries:
			res += min(0, t - end) + duration
			end = t + duration
		return res

a = Solution()
print(a.findPoisonedDuration([1,4],2))
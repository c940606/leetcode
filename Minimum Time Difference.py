class Solution(object):
	def findMinDifference(self, timePoints):
		"""
		给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。
		---
		输入: ["23:59","00:00"]
		输出: 1
		:type timePoints: List[str]
		:rtype: int
		"""
		n = len(timePoints)
		def helper(x):
			x=x.split(":")
			return int(x[0])*60 + int(x[1])

		timePoints = sorted(map(lambda x:helper(x),timePoints))
		print(timePoints)
		min_time = 1500
		for i in range(0,n-1):
			temp = timePoints[i+1] - timePoints[i]
			if temp < min_time:
				min_time = temp
		if abs(timePoints[0]+1440-timePoints[-1]) < min_time:
			min_time = abs(timePoints[0]+1440-timePoints[-1])
		return min_time
a = Solution()
print(a.findMinDifference(["23:59","00:00"]))


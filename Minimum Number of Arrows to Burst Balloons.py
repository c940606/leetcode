class Solution(object):
	def findMinArrowShots(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""
		points = sorted(points,key=lambda x:x[1])
		print(points)
		res = 0
		i = 0
		n = len(points)
		while i < n:
			flag = points[i][1]
			res += 1
			i += 1
			while i < n and flag >= points[i][0]:
				i += 1
		return res

a = Solution()
print(a.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))


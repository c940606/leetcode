class Solution:
	def minAreaFreeRect(self, points):
		"""
		:type points: List[List[int]]
		:rtype: float
		"""
		from itertools import combinations
		res = float("inf")
		lookup = {tuple(point) for point in points}
		# print(lookup)

		for a, b, c in combinations(points, 3):
			a = tuple(a)
			b = tuple(b)
			c = tuple(c)
			# print(a,b,c)
			# if a[0] == b[0] == c[0] or a[1] == b[1] == c[1]:
			# 	# print(",,.")
			# 	continue
			if (b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1]) == 0:
				d = (b[0] + c[0] - a[0], b[1] + c[1] - a[1])
				if d in lookup and d not in {a, b, c}:
					# bian1 = ((b[0] - a[0])**2 + (b[1] - a[1])**2) ** 0.5
					# bian2 = ((c[0] - a[0])**2+(c[1] - a[1])**2)**0.5
					area = (
						   ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) * ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)) ** 0.5
					# print(a,b,c,d,area)
					res = min(res, area)
			elif (c[0] - b[0]) * (a[0] - b[0]) + (c[1] - b[1]) * (a[1] - b[1]) == 0:
				d = (a[0] + c[0] - b[0], a[1] + c[1] - b[1])
				if d in lookup and d not in {a, b, c}:
					area = (
						   ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) * ((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)) ** 0.5
					# print(a, b, c, d, area)
					res = min(res, area)
			elif (a[0] - c[0]) * (b[0] - c[0]) + (a[1] - c[1]) * (b[1] - c[1]) == 0:
				d = (b[0] + a[0] - c[0], b[1] + a[1] - c[1])
				if d in lookup and d not in {a, b, c}:
					area = (
						   ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) * ((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)) ** 0.5
					# print(a, b, c, d, area)
					res = min(res, area)
		return res if res != float("inf") else 0


a = Solution()
print(a.minAreaFreeRect([[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]))
print(a.minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]))
print(a.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))
print(a.minAreaFreeRect([[0, 2], [0, 1], [3, 3], [1, 0], [2, 3], [1, 2], [1, 3]]))
print(a.minAreaFreeRect([[2,4],[4,2],[1,0],[3,4],[4,4],[2,2],[1,1],[3,0],[1,4],[0,3],[0,1],[2,1],[4,0]]))
print(a.minAreaFreeRect([[7,3],[8,12],[13,5],[6,2],[8,0],[12,8],[14,2],[2,6]]))
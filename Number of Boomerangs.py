class Solution(object):
	def numberOfBoomerangs(self, points):
		"""
		给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，
		其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
		找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
		---
		输入:
		[[0,0],[1,0],[2,0]]
		输出:
		2
		解释:
		两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
		---

		:type points: List[List[int]]
		:rtype: int
		"""
		n = len(points)
		if n < 3:
			return 0
		res = 0
		for i in range(n):
			lookup = {}
			for j in range(n):
				temp = (points[i][0] - points[j][0])**2 + (points[i][1]-points[j][1])**2
				if temp in lookup:
					lookup[temp] += 1
				else:
					lookup[temp] = 1
			for value in lookup.values():
				if value > 1:
					res += value*(value-1)
		return res
a = Solution()
print(a.numberOfBoomerangs([[0,0],[1,0],[2,0]]))

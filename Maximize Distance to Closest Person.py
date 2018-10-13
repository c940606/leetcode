class Solution(object):
	def maxDistToClosest(self, seats):
		"""
		在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
		至少有一个空座位，且至少有一人坐在座位上。
		亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
		返回他到离他最近的人的最大距离。
		---
		输入：[1,0,0,0,1,0,1]
		输出：2
		解释：
		如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
		如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
		因此，他到离他最近的人的最大距离是 2 。
		---
		输入：[1,0,0,0]
		输出：3
		解释：
		如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
		这是可能的最大距离，所以答案是 3 。
		---
		思路:
		1. 首尾 离最近的距离
		2. 中间 考虑 两个一之间距离
		:type seats: List[int]
		:rtype: int
		"""
		if not seats:
			return 0
		loc_seat = []
		n = len(seats)
		for i in range(n):
			if seats[i] == 1:
				loc_seat.append(i)
		beg = loc_seat[0]
		last = n-loc_seat[-1]-1
		print(beg,last)

		res = []
		for i in range(len(loc_seat)-1):
			temp = (loc_seat[i+1] - loc_seat[i])//2
			if temp > beg and temp > last:
				res.append(temp)
		if not res:
			return max(beg,last)
		else:
			return max(res)


a = Solution()
print(a.maxDistToClosest([1,0,0,0,1,0,1]))


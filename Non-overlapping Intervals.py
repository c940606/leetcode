# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def eraseOverlapIntervals(self, intervals):
		"""
			给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
			注意:
			可以认为区间的终点总是大于它的起点。
			区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
		---
		思路：
		贪心算法
		:type intervals: List[Interval]
		:rtype: int
		"""
		if not intervals:
			return 0
		intervals = sorted(map(lambda x:[x.start,x.end],intervals),key= lambda x:x[1])
		print(intervals)
		n = len(intervals)
		i = 0
		j = 1
		count = 0
		while j < n:
			if intervals[i][1]<=intervals[j][0]:
				i = j
				j += 1
			else:
				count += 1
				j += 1
		return  count

		# return intervals
interval1 = Interval(0,2)
interval2 = Interval(1,3)
interval3 = Interval(2,4)
interval4 = Interval(3,5)
interval5 = Interval(4,6)
intervals = [interval1,interval2,interval3,interval4,interval5]
a = Solution()
print(a.eraseOverlapIntervals(intervals))


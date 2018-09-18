# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
class Solution:
	def merge(self, intervals):
		"""
		输入: [[1,3],[2,6],[8,10],[15,18]]
		输出: [[1,6],[8,10],[15,18]]
		---
		输入: [[1,4],[4,5]]
		输出: [[1,5]]
		题目:给出一个区间的集合，请合并所有重叠的区间。
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		intervals = sorted(intervals,key = lambda x:x.start)
		i = 0
		j = 1
		while i < len(intervals) and j < len(intervals):
			if intervals[i].end>=intervals[j].start:

				temp = intervals.pop(j)
				# print(temp)
				if intervals[i].end < temp.end:
					intervals[i].end = temp.end



			else:
				i += 1
				j += 1
		return intervals

	def merge1(self, intervals):
		intervals = sorted(intervals,key=lambda x : x.start)
		res = []
		for interval in intervals:
			if not res or res[-1].end < interval.start:
				res.append(interval)
			else:
				res[-1].end = max(res[-1].end,interval.end)
		return res

a = Solution()
intervals1 = [[1,3],[2,6],[8,10],[15,18]]

intervals2 = [[1,4],[4,5]]
print(a.merge(intervals2))


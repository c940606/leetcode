class Solution:
	def minimumTotal(self, triangle):
		"""
		给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
		:type triangle: List[List[int]]
		:rtype: int
		"""
		index = 0
		res = []
		for item in triangle[::-1]:

			val = min([item[index],item[index+1]])
			print(val)
			res.append(val)
			index = item.index(val)
		return sum(res)
a = Solution()
t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
t1 = [[-1],[2,3],[1,-1,-3]]
print(a.minimumTotal(t1))

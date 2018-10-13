class Solution(object):
	def constructRectangle(self, area):
		"""
		作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。
		现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。
		要求：
		1. 你设计的矩形页面必须等于给定的目标面积。
		2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
		3. 长度 L 和宽度 W 之间的差距应当尽可能小。
		---
		输入: 4
		输出: [2, 2]
		解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
		但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
		:type area: int
		:rtype: List[int]
		"""
		flag = int(area**0.5)
		while True:
			if area % flag == 0:
				return [area//flag,flag]
			else:
				flag -= 1
a = Solution()
print(a.constructRectangle(5))

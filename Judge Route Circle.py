from collections import Counter


class Solution(object):
	def judgeCircle(self, moves):
		"""
		初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，
		判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到原来的位置。
		移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有 R（右），L（左），U（上）和 D（下）。
		输出应为 true 或 false，表示机器人移动路线是否成圈。
		---
		输入: "UD"
		输出: true
		---
		思路：
		左右 和 上下 出现的个数要相同的
		:type moves: str
		:rtype: bool
		"""
		loc = [0,0]
		for step in moves:
			if step == "U":
				loc[0] += 1
			if step == "D":
				loc[0] -= 1
			if step == "L":
				loc[1] -= 1
			if step == "R":
				loc[1] += 1
		return sum(loc) == 0
a = Solution()
print(a.judgeCircle("UDUDRL"))
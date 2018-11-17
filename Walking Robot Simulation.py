class Solution(object):
	def robotSim(self, commands, obstacles):
		"""
		机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
		-2：向左转 90 度
		-1：向右转 90 度
		1 <= x <= 9：向前移动 x 个单位长度
		在网格上有一些格子被视为障碍物。
		第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
		如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
		返回从原点到机器人的最大欧式距离的平方。
		---
		输入: commands = [4,-1,3], obstacles = []
		输出: 25
		解释: 机器人将会到达 (3, 4)
		---
		输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
		输出: 65
		解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
		:type commands: List[int]
		:type obstacles: List[List[int]]
		:rtype: int
		"""
		if not commands:return 0
		cur = [0,0]
		i = 0
		n = len(commands)
		# 1:bei 2:dong 3 nan   4 xi
		toward = 1
		while i < n:
			if commands[i] == -1:
				i = i+1
				step = commands[i]
				while step>0 and cur not in obstacles:

			elif commands[i] == -2:
				pass
			else:
				step = commands[i]
				if toward == 1:
					pass
				elif toward == 2:
					pass
				elif
				while step > 0 and cur not in obstacles:
					cur[1] += 1
					step -= 1
				i += 1

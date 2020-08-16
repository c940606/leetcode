from typing import List
import collections


class TreeAncestor:

	def __init__(self, n: int, parent: List[int]):
		cur_step = dict(enumerate(parent))
		self.step = 15
		jump = []
		jump.append(cur_step)
		for _ in range(self.step):
			next_jump = {}
			for node in cur_step:
				if cur_step[node] in cur_step:
					next_jump[node] = cur_step[cur_step[node]]
			jump.append(next_jump)
			cur_step = next_jump
		self.jump = jump



	def getKthAncestor1(self, node: int, k: int) -> int:
		step = self.step
		while k > 0 and node > -1:
			if k >= 1 << step:
				node = self.jump[step].get(node,-1)
				k -= k << step
			else:
				step -= 1
		return node
	def getKthAncestor(self, node: int, k: int) -> int:
		for i in range(self.step, -1, -1):
			if k & (1 << i):
				node = self.jump[i][node]
				if node == -1:
					break
		return node

class Solution:

	def __init__(self, w: List[int]):
		probability = [0] * len(w)
		_sum = sum(w)
		cur = 0
		for i in range(len(w)):
			cur += w[i]
			probability[i] = cur / _sum
		self.probability = probability


	def pickIndex(self) -> int:
		pass

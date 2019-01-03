class Solution(object):
	def prisonAfterNDays(self, cells, N):
		"""
		:type cells: List[int]
		:type N: int
		:rtype: List[int]
		"""
		circle = [cells]
		while N:
			tmp = [0] * 8
			for i in range(1, 7):
				tmp[i] = 1 if (circle[-1][i - 1] == 0 and circle[-1][i + 1] == 0) or (
					circle[-1][i - 1] == 1 and circle[-1][i + 1] == 1) else 0
			# print(tmp)
			if len(circle) > 1 and tmp == circle[1]:
				break
			circle.append(tmp)
			N -= 1
		if N == 0:
			return circle[-1]
		# print(N,tmp,circle)
		circle.pop(0)
		n = len(circle)
		yushu = (N - 1) % n
		return circle[yushu]


a = Solution()
print(a.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
print(a.prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))

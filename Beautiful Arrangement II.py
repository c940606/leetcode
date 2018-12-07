class Solution(object):
	def constructArray(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[int]
		"""
		from itertools import permutations
		for temp in permutations(range(1, n + 1)):
			print(temp)
			if len(set(map(lambda x: abs(x[0] - x[1]), zip(temp, temp[1:])))) == k:
				return list(temp)

	def constructArray1(self, n, k):
		low = 1
		high = n
		res = [0] * n
		# cou = 0
		for i in range(n):
			if k > 1:
				if k % 2 != 0:
					res[i] = low
					low += 1
				else:
					res[i] = high
					high -= 1
				k -= 1
			else:
				res[i] = low
				low += 1
		return res




a = Solution()
print(a.constructArray1(n=5, k=2))
print(a.constructArray1(n=3, k=2))

print(a.constructArray1(10, 4))

# a = Solution()
# print(a.constructArray(3, 2))
# print(a.constructArray1(92, 80))

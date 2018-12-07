class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		"""
		:type n: int
		:type primes: List[int]
		:rtype: int
		"""
		num = len(primes)
		multiplier = [0] * num
		res = [1]
		while n > 1:
			res.append(min(map(lambda x:res[x[1]]*x[0],zip(primes,multiplier))))
			for i in range(num):
				if res[-1] // res[multiplier[i]] == primes[i]:
					multiplier[i] += 1
			n -= 1
		print(res)
		return res[-1]
a = Solution()
print(a.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
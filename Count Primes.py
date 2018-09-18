class Solution(object):
	def countPrimes(self, n):
		"""
		统计所有小于非负整数 n 的质数的数量。
		--
		输入: 10
		输出: 4
		解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
		---

		:type n: int
		:rtype: int
		"""
		isPrime = [1 for i in range(n)]
		i = 2
		while i < int(n**0.5)+1:
			j = i * i
			while j < n:
				isPrime[j] = 0
				j += i
			i += 1
		return sum(isPrime[2:])
a = Solution()
print(a.countPrimes(10))
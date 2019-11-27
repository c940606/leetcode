class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        import  math
        mod = 10 ** 9 + 7
        if n <= 2: return 1
        def helper(n):
            if n < 2: return 0
            isPrimes = [1] * n
            isPrimes[0] = isPrimes[1] = 0
            for i in range(2, int(n ** 0.5) + 1):
                if isPrimes[i] == 1:
                    isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
            return sum(isPrimes)
        tmp = helper(n + 1)
        print(tmp)
        return (math.factorial(tmp) * math.factorial(n - tmp)) % mod

a = Solution()
# print(a.numPrimeArrangements(5))
# print(a.numPrimeArrangements(100))
# print(a.numPrimeArrangements(2))
print(a.numPrimeArrangements(11))
class Solution(object):
    def countPrimes1(self, n):
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
        while i < int(n ** 0.5) + 1:
            j = i * i
            while j < n:
                isPrime[j] = 0
                j += i
            i += 1
        return sum(isPrime[2:])

    def countPrimes2(self, n):
        res = 0
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                # print(i)
                res += 1
        return res

    def countPrimes5(self, n):
        res = 0
        for i in range(2, n):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                # print(i)
                res += 1
        return res

    def countPrimes6(self, n):
        isPrimes = [1] * n
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1: res += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return res

    def countPrimes(self, n):
        if n < 2: return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)


a = Solution()
print(a.countPrimes(100))

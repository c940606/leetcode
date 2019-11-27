from typing import List


class Solution(object):
    def nthSuperUglyNumber1(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        num = len(primes)
        multiplier = [0] * num
        res = [1]
        while n > 1:
            res.append(min(map(lambda x: res[x[1]] * x[0], zip(primes, multiplier))))
            for i in range(num):
                if res[-1] // res[multiplier[i]] == primes[i]:
                    multiplier[i] += 1
            n -= 1
        print(res)
        return res[-1]

    def nthSuperUglyNumber2(self, n: int, primes: List[int]) -> int:

        uglies = [0] * n
        primes_to_uglies_loc = [0] * len(primes)
        uglies[0] = 1
        for i in range(1, n):
            uglies[i] = min(x * uglies[y] for x, y in zip(primes, primes_to_uglies_loc))
            for j in range(len(primes)):
                if uglies[i] >= primes[j] * uglies[primes_to_uglies_loc[j]]:
                    primes_to_uglies_loc[j] += 1
        return uglies[-1]

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        uglies = [0] * n
        uglies[0] = 1
        visited = set()
        visited.add(1)
        primes_to_uglies_loc = [0] * len(primes)
        heap = []
        for idx, prime in enumerate(primes):
            heapq.heappush(heap, [prime, idx])
            visited.add(prime)

        for i in range(1, n):
            uglies[i], k = heapq.heappop(heap)

            while primes[k] * uglies[primes_to_uglies_loc[k]] in visited:
                primes_to_uglies_loc[k] += 1
            heapq.heappush(heap, [primes[k] * uglies[primes_to_uglies_loc[k]], k])
            visited.add(primes[k] * uglies[primes_to_uglies_loc[k]])
        return uglies[-1]

a = Solution()
print(a.nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))
print(a.nthSuperUglyNumber1(n=12, primes=[2, 7, 13, 19]))

class Solution(object):
    def nthUglyNumber1(self, n):
        """
        编写一个程序，找出第 n 个丑数。
        丑数就是只包含质因数 2, 3, 5 的正整数。
        --
        输入: n = 10
        输出: 12
        解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
        ---
        思路：

        :type n: int
        :rtype: int
        """
        res = [1]
        num_2 = 0
        num_3 = 0
        num_5 = 0
        while n > 1:
            res.append(min(res[num_2] * 2, res[num_3] * 3, res[num_5] * 5))
            # print(res[-1])
            if res[-1] // res[num_2] == 2:
                num_2 += 1
            if res[-1] // res[num_3] == 3:
                num_3 += 1
            if res[-1] // res[num_5] == 5:
                num_5 += 1
            n -= 1
        return res[-1]

    def nthUglyNumber2(self, n):
        import heapq
        heap = [1]
        heapq.heapify(heap)
        res = 0
        visited = set()
        while n:
            res = heapq.heappop(heap)
            # print(res)
            a, b, c = res * 2, res * 3, res * 5
            for t in [a, b, c]:
                if t not in visited:
                    visited.add(t)
                    heapq.heappush(heap, t)
            n -= 1
        return res

    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]


a = Solution()
print(a.nthUglyNumber(10))
print(a.nthUglyNumber(1))

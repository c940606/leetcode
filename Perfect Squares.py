class Solution(object):
    def numSquares3(self, n):
        """
        给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
        使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
        ---
        输入: n = 12
        输出: 3
        解释: 12 = 4 + 4 + 4.
        --
        输入: n = 13
        输出: 2
        解释: 13 = 4 + 9.
        --
        思路:

        :type n: int
        :rtype: int
        """
        num = int(n ** 0.5)
        num_list = [i ** 2 for i in range(num, 0, -1)]
        res = []
        self.min_count = n + 1

        def helper(n, temp, count):
            if n < 0:
                return
            if n == 0:
                res.append(temp)
                self.min_count = min(self.min_count, count)
                return
            for num in num_list:
                helper(n - num, temp + [num], count + 1)

        helper(n, [], 0)
        print(self.min_count)
        return res

    def numSquares1(self, n):
        num = int(n ** 0.5)
        num_list = [i ** 2 for i in range(num, 0, -1)]
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            min_num = n + 1
            for num in num_list:
                if i - num >= 0 and res[i - num] + 1 < min_num:
                    min_num = res[i - num] + 1
            res[i] = min_num
        return res[-1]

    _dp = [0]

    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = self._dp
        while len(dp) <= n:
            print(list((min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,)))
            dp += list((min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,))
            print(dp)
        return dp[n]

    def numSquares4(self, n):
        from collections import deque
        if n == 0: return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    diff = tmp - i ** 2
                    if diff == 0:
                        return step
                    if diff not in visited:
                        visited.add(diff)
                        queue.appendleft(diff)
        return step

    def numSquares5(self, n):
        from collections import defaultdict
        # dp = defaultdict(lambda :float("inf"))
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        # print(dp)
        return dp[n]

    def numSquares(self, n):
        if n <= 0: return 0
        dp = [0]
        while len(dp) <= n:
            m = len(dp)
            tmp = float("inf")
            for i in range(1, int(m ** 0.5) + 1):
                tmp = min(tmp, dp[m - i * i] + 1)
            dp.append(tmp)
        return dp[-1]


a = Solution()
print(a.numSquares(12))
print(a.numSquares(8405))
print(a.numSquares(8935))

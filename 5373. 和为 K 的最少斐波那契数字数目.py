class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        import  functools
        dp = [1, 1]

        while dp[-1] < k:
            dp.append(dp[-1] + dp[-2])
        dp = dp[::-1]
        self.res = float("inf")

        def dfs(i, num, amount):
            if amount == 0:
                self.res = min(self.res, num)
                return
            for j in range(i, len(dp)):
                if (self.res - num) * dp[j] < amount:
                    break
                if dp[j] > amount:
                    continue
                dfs(j, num + 1, amount - dp[j])

        for i in range(len(dp)):
            dfs(i, 0, k)
        return self.res


a = Solution()
print(a.findMinFibonacciNumbers(5))
print(a.findMinFibonacciNumbers(603928666))
print(a.findMinFibonacciNumbers(855250767))
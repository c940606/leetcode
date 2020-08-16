class Solution:
    def leastOpsExpressTarget1(self, x: int, target: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(target):
            if x > target:
                return min(2 * target - 1, (x - target) * 2)
            if target == x:
                return 0
            sums = x
            times = 0
            while sums < target:
                times += 1
                sums *= x
            if sums == target:
                return times
            a = float("inf")
            b = float("inf")
            if sums - target < target:
                a = dfs(sums - target) + times
            b = dfs(target - (sums // x)) + times - 1
            return min(a, b) + 1

        return dfs(target)

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(cur):
            # 当cur < x, 比如 cur = 2, x = 3, 需要判断使用 3/3 + 3/3 和 3 - 3/3,哪个用运算符最少
            if cur < x:
                return min(2 * cur - 1, (x - cur) * 2)
            if cur == 0:
                return 0
            # 到cur 需要几个x相乘,
            p = int(math.log(cur, x))
            sums = x ** p
            # cur < sums 的情况,就是要加
            ans = dfs(cur - sums) + p
            # sums > cur, 就是要减去多少才能到底目标值, 这个判断条件是有严格的数学证明的
            if sums * x - cur < cur:
                ans = min(ans, p + 1 + dfs(sums * x - cur))
            return ans

        return dfs(target)


a = Solution()
print(a.leastOpsExpressTarget(3, 19))
print(a.leastOpsExpressTarget(5, 501))

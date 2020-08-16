class Solution:
    def numOfWays1(self, n: int) -> int:
        color2 = 6
        color3 = 6
        for i in range(2, n + 1):
            tmp = color3
            color3 = (2 * color3 + 2 *
                      color2) % 1000000007
            color2 = (2 * tmp + 3 *
                      color2) % 1000000007
        return (color2 + color3) % 1000000007

    def numOfWays(self, n: int) -> int:
        import functools
        colors = [1, 2, 3]

        @functools.lru_cache(None)
        def dfs(n, a, b, c):
            if n == 0: return 1
            res = 0
            for a1 in colors:
                if a == a1: continue
                for b1 in colors:
                    if b1 == a1 or b == b1: continue
                    for c1 in colors:
                        if b1 == c1 or c1 == c: continue
                        res += dfs(n - 1, a1, b1, c1) % 1000000007

            return res % 1000000007

        return dfs(n, 0, 0, 0)


a = Solution()
print(a.numOfWays(2))

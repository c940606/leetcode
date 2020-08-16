class Solution:
    def smallestGoodBase1(self, n: str) -> str:
        import math
        n = int(n)
        res = n - 1

        for s in range(59, 1, -1):
            k = int(n ** (1/s))
            if k > 1:
                _sum = 1
                mul = 1
                for _ in range(s):
                    mul *= k
                    _sum += mul
                if _sum == n:
                    res = k
                    break
        return str(res)

    def smallestGoodBase(self, n: str) -> str:
        import math
        n = int(n)
        res = n - 1
        for m in range(int(math.log2(n)), 0, -1):
            left = 2
            right = int(n ** (1/m)) + 1
            while left <= right:
                _sum = 1
                mid = (left + right) // 2
                for _ in range(m):
                    _sum = _sum * mid + 1
                if _sum == n:
                    return str(mid)
                elif _sum < n:
                    left = mid + 1
                else:
                    right = mid - 1
        return str(res)

a = Solution()
print(a.smallestGoodBase("4681"))
print(a.smallestGoodBase(str(10**18)))
print(a.smallestGoodBase("13"))
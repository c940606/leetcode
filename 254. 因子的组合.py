class Solution:
    def getFactors(self, n: int):
        res = []
        def helper(n, i, tmp):
            if n == 1:
                if len(tmp) > 1:
                    res.append(tmp)
            else:
                for j in range(i, n + 1):
                    if n % j == 0:
                        helper(n // j, j, tmp + [j])
        helper(n, 2, [])
        return res


a = Solution()
print(a.getFactors(1))
print(a.getFactors(37))
print(a.getFactors(12))
print(a.getFactors(32))

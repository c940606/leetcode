class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        from collections import defaultdict
        import math
        lookup = defaultdict(int)

        for x, y in dominoes:
            lookup[tuple(sorted([x, y]))] += 1

        print(lookup)

        def cal(num):
            if num < 2: return 0
            return (math.factorial(num )) // (math.factorial(2) * math.factorial(num - 2))

        print(cal(3))
        res = 0
        for n in lookup.values():
            res += cal(n)
        return res


a = Solution()
print(a.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
print(a.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))

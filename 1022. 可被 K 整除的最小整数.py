class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        n = len(str(K))
        lookup = set()
        i = n
        s = "1" * n
        while i <= K:
            num = int(s)
            y = num % K
            if y in lookup:
                break
            if num >= K and y == 0:
                return i
            lookup.add(y)
            s += "1"
            i += 1
        return -1

    def smallestRepunitDivByK1(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0: return -1
        r = 0
        for N in range(1, K + 1):
            r = (r * 10 + 1) % K
            print(r)
            if r == 0:return N
        return -1


a = Solution()
# print(a.smallestRepunitDivByK1(1))
# print(a.smallestRepunitDivByK1(2))
# print(a.smallestRepunitDivByK1(3))
# print(a.smallestRepunitDivByK1(19927))
print(a.smallestRepunitDivByK1(39))
# print(a.smallestRepunitDivByK1(49997))

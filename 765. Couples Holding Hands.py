class Solution:
    def minSwapsCouples(self, row):
        f = {}
        n = len(row)
        N = n // 2
        self.count = N

        def find(x):
            f.setdefault(x, x)
            while f[x] != x:
                x = f[x]
            return x

        def union(x, y):
            tmp1 = find(x)
            tmp2 = find(y)
            if tmp1 != tmp2:
                f[find(x)] = find(y)
                self.count -= 1

        for i in range(N):
            p1 = row[2 * i]
            p2 = row[2 * i + 1]
            union(p1 // 2, p2 // 2)
        return N - self.count

    def minSwapsCouples1(self, row):
        n = len(row)
        res = 0
        for i in range(0, n, 2):
            t = row[i] ^ 1
            j = row.index(t)
            if j - i > 1:
                row[i + 1], row[j] = row[j], row[i + 1]
                res += 1
        return res


a = Solution()
print(a.minSwapsCouples1(row=[0, 2, 1, 3]))
print(a.minSwapsCouples1(row=[3, 2, 0, 1]))

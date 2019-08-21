class Solution:
    def earliestAcq(self, logs, N):
        logs.sort()
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        for i in range(N):
            find(i)
        #print(f)
        for time, x, y in logs:
            union(x, y)
            if len(set(map(find, f))) == 1:
                return time
        return -1



a = Solution()
print(a.earliestAcq(
    logs=[[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
          [20190312, 1, 2], [20190322, 4, 5]], N=6))

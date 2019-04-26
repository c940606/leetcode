class Solution:
    def assignBikes(self, workers, bikes):
        from collections import defaultdict
        lookup = defaultdict(list)
        n = len(workers)
        m = len(bikes)
        for i in range(n):
            for j in range(m):
                x, y = workers[i]
                s, t = bikes[j]
                lookup[abs(x - s) + abs(y - t)].append((i,j))
        #print(lookup)
        key_num = sorted(list(lookup.keys()))
        workers_visited = set()
        bikes_visited = set()
        res = [None] * n
        for num in key_num:
            for x, y in lookup[num]:
                if x not in workers_visited and y not in bikes_visited:
                    res[x] = y
                    workers_visited.add(x)
                    bikes_visited.add(y)
        return res


a = Solution()
print(a.assignBikes(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))
print(a.assignBikes(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]))

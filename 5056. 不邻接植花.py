class Solution:
    def gardenNoAdj(self, N, paths):
        from collections import defaultdict
        res = [0] * N
        graph = defaultdict(set)
        for path in paths:
            graph[path[0]].add(path[1])
            graph[path[1]].add(path[0])

        def connected_grade(i):
            ans = []
            for g in graph[i]:
                if res[g - 1] != 0:
                    ans.append(res[g - 1])
            return ans

        for i in range(1, N + 1):
            tmp = connected_grade(i)
            flower = 1
            while flower in tmp:
                flower += 1
            res[i - 1] = flower
        return res


a = Solution()
print(a.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]))
print(a.gardenNoAdj(4, [[1, 2], [3, 4]]))
print(a.gardenNoAdj(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))

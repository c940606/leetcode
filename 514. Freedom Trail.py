class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections, functools
        lookup = collections.defaultdict(list)
        # steps = collections.defaultdict(int)
        for i in range(len(ring)):
            # tmp = ring[i:] + ring[:i]
            lookup[ring[i]].append(i)
            # steps[tmp] = i

        def cal_steps(cur, nxt):
            return min(tmp := abs(steps[cur] - steps[nxt]), len(ring) - tmp)

        @functools.lru_cache(None)
        def dfs(cur, k):
            if k == len(key):
                return 0
            res = float("inf")
            for j in lookup[key[k]]:
                res = min(res, min(tmp:= abs(cur - j), len(ring) - tmp) + 1 + dfs(j, k + 1))
            return res

        return dfs(0, 0)


a = Solution()
print(a.findRotateSteps(ring="godding", key="gd"))

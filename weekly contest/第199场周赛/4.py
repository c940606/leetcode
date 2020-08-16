class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        from itertools import groupby
        import functools

        res = ""
        for t, v in groupby(s):
            l = len(list(v))
            if l == 1:
                res += t
            else:
                res += t + str(l)

        # print(res)
        @functools.lru_cache(None)
        def dfs(i, j, k):
            # print(s, k)

            if len(set(s)) == len(s):
                return len(s) - k
            res = ""
            for t, v in groupby(s):
                l = len(list(v))
                if l == 1:
                    res += t
                else:
                    res += t + str(l)
            # print(res)
            ans = len(res)
            if k == 0:
                return ans
            for m in range(i, j):
                # print(s[:i] + s[i + 1:])
                ans = min(ans, dfs(s[:i] + s[i + 1:], k - 1))
            # print(ans)
            return ans

        return dfs(s, k)


a = Solution()
print(a.getLengthOfOptimalCompression(s="aaabcccd", k=2))
print(a.getLengthOfOptimalCompression(s="aabbaa", k=2))
print(a.getLengthOfOptimalCompression("abcdefghijklmnopqrstuvwxyz", 16))

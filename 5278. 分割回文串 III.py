class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        import functools
        if len(s) == k: return 0

        def cal(s):
            n = len(s)
            cost = 0
            for i in range(n // 2):
                if s[i] != s[n - i - 1]:
                    cost += 1
            return cost

        @functools.lru_cache(None)
        def helper(s, k):
            if len(s) == k:
                return 0
            if k == 1:
                return cal(s)
            res = float("inf")
            for i in range(len(s)):
                cur = cal(s[:i + 1]) + helper(s[i + 1:], k - 1)
                res = min(res, cur)

            return res

        return helper(s, k)


a = Solution()
print(a.palindromePartition("abc", 2))
print(a.palindromePartition(s="aabbc", k=3))

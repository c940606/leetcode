class Solution:
    def longestSubsequence1(self, arr, difference: int) -> int:
        from collections import Counter
        if difference == 0:
            return max(Counter(arr).values())
        res = 0
        ar = set(arr)
        for a in ar:
            if a - difference not in ar:
                c = 1
                while a + difference in ar:
                    a += difference
                    c += 1
                res = max(c, res)
        return res

    def longestSubsequence(self, arr, difference: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        res = 1
        for a in arr:
            dp[a] = dp[a - difference] + 1
            res = max(res, dp[a])
        return res


a = Solution()
print(a.longestSubsequence([7, -2, 8, 10, 6, 18, 9, -8, -5, 18, 13, -6, -17, -1, -6, -9, 9, 9], 1))
print(a.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
print(a.longestSubsequence(arr=[1, 3, 5, 7], difference=1))
print(a.longestSubsequence(arr=[1, 2, 3, 4], difference=1))
print(a.longestSubsequence(arr=[1, 1], difference=0))
print(a.longestSubsequence([3, 0, -3, 4, -4, 7, 6], 3))

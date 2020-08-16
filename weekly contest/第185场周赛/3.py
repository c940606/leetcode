class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = {"a": 3, "r": 1, "o": 2, "c": 0, "k": 4}
        dp = [0] * 5
        res = -1
        for s in croakOfFrogs:
            loc = c[s]
            dp[loc] += 1
            # print(dp)
            if max(dp[:loc], default=float("inf")) < dp[loc]: return -1
            if (tmp := min(dp)) != 0:
                res = max(res, max(dp))
                for i in range(5):
                    dp[i] -= tmp
            # if len(set(dp)) == 1:
            #     res = max(res, dp[0])
            #     dp = [0] * 5
        return res if len(set(dp)) == 1 else -1


a = Solution()
print(a.minNumberOfFrogs("croakcroak"))
print(a.minNumberOfFrogs("crcoakroak"))
print(a.minNumberOfFrogs("croakcrook"))
print(a.minNumberOfFrogs("croakcroa"))
print(a.minNumberOfFrogs("croak"))
print(a.minNumberOfFrogs("croakcroa"))
print(a.minNumberOfFrogs("crocakcroraoakk"))

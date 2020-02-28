from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [0]
        for a in arr:
            dp.append(dp[-1] ^ a)
        # print(dp)
        res = []
        for a, b in queries:
            res.append(dp[b + 1] ^ dp[a])
        return res

a = Solution()
print(a.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
print(a.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))
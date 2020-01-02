from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        dp = [0] * n
        dp[-1] = -1
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], arr[i + 1])
        return dp

a = Solution()
print(a.replaceElements(arr = [17,18,5,4,6,1]))
print(a.replaceElements(arr=[1]))
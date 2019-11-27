from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # dp[i][j] 表示 前i个硬币j个为正的概率
        dp = [[0] * (target + 1) for _ in range(len(prob) + 1)]

        dp[0][0] = 1.0

        for i in range(1, len(prob) + 1):
            for j in range(1, min(i, target) + 1):
                dp[i][j] = dp[i - 1][j - 1] * prob[i - 1] + dp[i - 1][j] * (1 - prob[i - 1])
            dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])
        # print(dp)
        return dp[-1][-1]


a = Solution()
print(a.probabilityOfHeads([0.4], 1))
print(a.probabilityOfHeads(prob=[0.5, 0.5, 0.5, 0.5, 0.5], target=0))

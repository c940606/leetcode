from typing import List, Any


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """:arg
      鸡蛋\楼 1    2    3   4   5   6
        1    1    2    3   4   5   6
        2    1    2    

        """
        # dp[i][j] 第i个鸡蛋在j层需要最少步数
        dp: List[List[Any]] = [[float("inf")] * (N + 1) for _ in range(K + 1)]

        # 行
        for j in range(1, N + 1):
            dp[1][j] = j
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        # pprint(dp)

        # for i in range(2, K + 1):
        #     for j in range(2, N + 1):
        #         for k in range(1, j + 1):
        #             dp[i][j] = min(dp[i][j], max(dp[i - 1][k - 1], dp[i][j - k]) + 1)

        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k < j and dp[i - 1][k - 1] < dp[i][j - k]:
                    k += 1
                dp[i][j] = 1 + dp[i - 1][k - 1]
        return dp[K][N]


a = Solution()
print(a.superEggDrop(3, 16))

class Solution:
    def minimumTotal1(self, triangle):
        """
        给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
        :type triangle: List[List[int]]
        :rtype: int
        ---
        [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
        ]
        自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
        ---
        思路:
        先建立和题中构造一样的结构
        1.边界
            直接上一个边界加上来就行
        2. 中间
            同一位置 和 旁边位置最小值
        """
        n = len(triangle)
        if n == 0:
            return 0
        dp = [[0] * i for i in range(1, n + 1)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for k in range(i + 1):
                if k == 0:
                    dp[i][k] = dp[i - 1][k] + triangle[i][k]
                elif k == i:
                    dp[i][k] = dp[i - 1][k - 1] + triangle[i][k]
                else:
                    dp[i][k] = min(dp[i - 1][k - 1], dp[i - 1][k]) + triangle[i][k]
        return min(dp[-1])

    def minimumTotal2(self, triangle) -> int:
        import functools
        row = len(triangle)

        @functools.lru_cache(None)
        def helper(level, i, j):
            if level == row:
                return 0
            res = 0
            a = float("inf")
            b = float("inf")
            if 0 <= i < len(triangle[level]):
                a = helper(level + 1, i, i + 1) + triangle[level][i]
            if 0 <= j < len(triangle[level]):
                b = helper(level + 1, j, j + 1) + triangle[level][j]
            res += min(a, b)
            return res

        return helper(0, -1, 0)

    def minimumTotal(self, triangle) -> int:
        row = len(triangle)
        dp = [0] * row
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        #print(dp)
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


a = Solution()
t = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
t1 = [[-1], [2, 3], [1, -1, -3]]
print(a.minimumTotal(t))

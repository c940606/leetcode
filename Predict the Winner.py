class Solution(object):
    def PredictTheWinner3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = {}

        def helper(_sum, start, end):
            if (start, end) in lookup:
                return lookup[(start, end)]
            if start == end:
                lookup[(start, end)] = nums[start]
                return nums[start]

            score1 = _sum - helper(_sum - nums[start], start + 1, end)
            print("score1:", score1)
            score2 = _sum - helper(_sum - nums[end], start, end - 1)
            print("score2:", score2)
            res = max(score1, score2)
            print(start, end, res)
            lookup[(start, end)] = res
            return res

        return helper(sum(nums), 0, len(nums) - 1) * 2 >= sum(nums)

    def PredictTheWinner1(self, nums):

        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for j in range(1, n):
            for k in range(0, n - j):
                s = k + j
                dp[k][s] = max(nums[k] - dp[k + 1][s], nums[s] - dp[k][s - 1])
        print(dp)
        return dp[0][n - 1] >= 0

    def PredictTheWinner(self, nums):
        import functools
        left = 0
        right = len(nums) - 1

        @functools.lru_cache(None)
        def helper(left, right):
            if left > right:
                return 0

            return max(
                nums[left] + min(helper(left + 2, right), helper(left + 1, right - 1)),
                nums[right] + min(helper(left + 1, right - 1), helper(left, right - 2))
            )
        tmp = helper(left, right)
        print(tmp)
        return helper(left, right) >= sum(nums) / 2


a = Solution()
print(a.PredictTheWinner([0]))
print(a.PredictTheWinner([1, 2, 5]))

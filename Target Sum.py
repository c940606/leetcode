class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        self.res = 0

        def helper(idx, S):

            if idx == n:
                if S == 0:
                    self.res += 1
                return
            helper(idx + 1, S + nums[idx])
            helper(idx + 1, S - nums[idx])

        helper(0, S)
        return self.res

    def findTargetSumWays1(self, nums, S):
        lookup = {}
        n = len(nums)

        def helper(i, j, S):
            if i == n:
                if S == 0:
                    return 1
                return 0
            if (i, j, S) in lookup:
                return lookup[(i, j, S)]
            a = helper(i + 1, j, S - nums[i])
            b = helper(i + 1, j, S + nums[i])
            res = a + b
            lookup[(i, j, S)] = res
            # print(lookup)
            return res

        helper(0, n, S)
        print(lookup)
        return helper(0, n, S)

    def findTargetSumWays2(self, nums, S):
        from collections import defaultdict
        count1 = defaultdict(int)
        count1[0] = 1
        for num in nums:
            count2 = defaultdict(int)
            for tmp_sum in count1:
                count2[tmp_sum - num] += count1[tmp_sum]
                count2[tmp_sum + num] += count1[tmp_sum]
            count1 = count2
        return count1[S]

    def findTargetSumWays3(self, nums, S):
        sum_nums = sum(nums)

        # print(sum_nums)
        def helper(tmp):

            dp = [0] * (tmp + 1)
            dp[0] = 1

            for num in nums:
                for i in range(tmp, num - 1, -1):
                    dp[i] += dp[i - num]

            return dp[tmp]

        return 0 if sum_nums < S or (S + sum_nums) % 2 != 0 else helper((S + sum_nums) // 2)


a = Solution()
print(a.findTargetSumWays3([1, 1, 1, 1, 1], 3))
print(a.findTargetSumWays3([2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48, 12, 38], 48))

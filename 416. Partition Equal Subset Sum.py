class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        sum_nums = sum(nums)

        if sum_nums % 2 != 0:
            return False
        avg = sum_nums // 2
        nums.sort()
        n = len(nums)

        dp = [[1] + [0] * avg for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, avg + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    if dp[i][j] == 0 and dp[i - 1][j - nums[i - 1]] == 1:
                        dp[i][j] = 1
        # print(dp)
        return True if dp[-1][-1] == 1 else False

    def canPartition1(self, nums: 'List[int]') -> 'bool':
        sum_nums = sum(nums)

        if sum_nums % 2 != 0:
            return False
        avg = sum_nums // 2
        nums.sort(reverse=True)
        print(nums)
        n = len(nums)

        def dfs(remain, loc):
            # print("remian:",remain)
            if remain == 0:
                return True
            if (loc < n and remain < nums[loc]):
                return False
            # if remain<0:
            #     return False
            for i in range(loc, n):
                if dfs(remain - nums[i], i + 1):
                    return True
            return False

        return dfs(avg, 0)


a = Solution()
print(a.canPartition1([1, 2, 5]))
print(a.canPartition1([1, 5, 11, 5, 2]))
print(a.canPartition1([1, 2, 3, 5]))
# print(a.canPartition([1,1]))
# print(a.canPartition([1,2,3,4,5,6,7]))
print(a.canPartition1(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]))
print(a.canPartition1(
    [19, 33, 38, 60, 81, 49, 13, 61, 50, 73, 60, 82, 73, 29, 65, 62, 53, 29, 53, 86, 16, 83, 52, 67, 41, 53, 18, 48, 32,
     35, 51, 72, 22, 22, 76, 97, 68, 88, 64, 19, 76, 66, 45, 29, 95, 24, 95, 29, 95, 76, 65, 35, 24, 85, 95, 87, 64, 97,
     75, 88, 88, 65, 43, 79, 6, 5, 70, 51, 73, 87, 76, 68, 56, 57, 69, 77, 22, 27, 29, 12, 55, 58, 18, 30, 66, 53, 53,
     81, 94, 76, 28, 41, 77, 17, 60, 32, 62, 62, 88, 61]))

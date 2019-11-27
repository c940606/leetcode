class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        cur = 0
        res = 0
        for num in nums:
            if num % 2 == 1:
                cur += 1
            if cur >= k:
                res += dp[cur - k]
            dp[cur] += 1
        return res

a = Solution()
print(a.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
print(a.numberOfSubarrays(nums = [2,4,6], k = 1))
print(a.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))

class Solution:
    def missingElement(self, nums, k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] + k
        dp = [0]
        for i in range(1, n):
            dp.append(dp[-1] + nums[i] - nums[i - 1] - 1)
            #print(dp)

            if dp[-1] >= k:
                return nums[i - 1] + k - dp[-2]

        return nums[-1] + k - dp[-1]

a = Solution()
print(a.missingElement([4,7,9,10],  1))
print(a.missingElement([4,7,9,10], 3))
print(a.missingElement([1,2,4],  3))

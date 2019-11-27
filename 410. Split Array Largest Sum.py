class Solution:
    def splitArray(self, nums, m: int) -> int:
        if not nums: return 0
        left = max(sum(nums) // m, max(nums))
        right = sum(nums)

        def helper(mid):
            c = 1
            t = nums[0]
            for num in nums[1:]:
                if t + num <= mid:
                    t += num
                else:
                    # print(t)
                    c += 1
                    t = num
            return c

        # print(helper(16))
        while left < right:
            mid = left + (right - left) // 2
            # print(mid, helper(mid))
            if helper(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
# print(a.splitArray([7, 2, 5, 10, 8], 2))
print(a.splitArray([1,2147483647],2))
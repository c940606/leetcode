class Solution:
    def pathSum(self, nums) -> int:
        lookup = {}
        if not nums: return 0
        self.res = 0
        for num in nums:
            lookup[num // 10] = num % 10

        def helper(num, cur):
            depth = num // 10
            pos = num % 10
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1
            cur += lookup[num]
            if left not in lookup and right not in lookup:
                self.res += cur
                return
            if left in lookup:
                helper(left, cur)
            if right in lookup:
                helper(right, cur)

        helper(nums[0] // 10, 0)
        return self.res

a = Solution()
print(a.pathSum([113, 215, 221]))

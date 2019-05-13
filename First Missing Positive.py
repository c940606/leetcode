class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        lookup = {}
        for num in nums:
            lookup[num] = 1
        for i in range(1, len(nums) + 1):
            if i not in lookup:
                return i

    def firstMissingPositive1(self, nums):
        i = 1
        while True:
            if i not in nums:
                return i
            else:
                i += 1

    def firstMissingPositive2(self, nums):

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        #print(nums)
        i = 0
        while i + 1 == nums[i]:
            i += 1
        return i + 1


a = Solution()
print(a.firstMissingPositive2([1, 2, 0]))
print(a.firstMissingPositive2([3, 4, -1, 1]))

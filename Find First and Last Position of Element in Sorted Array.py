class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        n = len(nums)
        if target in nums:
            res[0] = nums.index(target)
            res[1] = n-nums[::-1].index(target)-1
        return res
a = Solution()
print(a.searchRange([1,1,34],2))
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        flag = sorted(nums)[n//2]
        return sum(map(lambda x:abs(x-flag),nums))
a = Solution()
print(a.minMoves2([1,2,3]))
class Solution:
    def canDivideIntoSubsequences(self, nums, K):
        from collections import Counter
        c = Counter(nums)
        nums_s = sorted([v, k] for k, v in c.items())[::-1]
        #print(nums)
        return nums_s[0][0] * K <= len(nums)


a = Solution()
print(a.canDivideIntoSubsequences(nums=[1, 2, 2, 3, 3, 4, 4], K=3))

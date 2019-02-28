class Solution:
    def findSubsequences(self, nums: 'List[int]') -> 'List[List[int]]':
        self.res = set()
        n = len(nums)
        def helper(loc,tmp):
            if len(tmp) > 1 and tmp not in self.res:
                self.res.add(tmp)
            for i in range(loc+1,n):
                if tmp[-1] <= nums[i]:
                    helper(i,tmp+(nums[i],))
        for i in range(n):
            helper(i,(nums[i],))
        return [list(i) for i in self.res]
a = Solution()
print(a.findSubsequences([4,6,7,7]))
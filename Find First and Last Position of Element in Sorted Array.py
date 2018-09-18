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

    def searchRange1(self, nums, target):
        if not nums:
            return [-1,-1]
        n = len(nums)
        left,right = 0,n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                left = mid
                right = mid
                while left > 0 and nums[left-1] == target:
                    left -= 1

                while right < n-1 and nums[right+1] == target:
                    right += 1

                return [left,right]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left  = mid + 1
        return [-1,-1]



a = Solution()
print(a.searchRange1([0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11],0))
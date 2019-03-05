class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        n = len(nums)
        for i in range(1,n,2):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    nums[j],nums[i] = nums[i],nums[j]
                    break
            if i == 1 and n > 2:
                nums[i + 1], nums[i - 1] = nums[i - 1], nums[i + 1]
            if 1<i < n-1 and nums[i-2]!=nums[i+1]:
                nums[i+1],nums[i-1] = nums[i-1],nums[i+1]
            print(nums)



a = Solution()
print(a.wiggleSort(nums = [1, 5, 1, 1, 6, 4]))
print(a.wiggleSort(nums = [1, 3, 2, 2, 3, 1]))
print(a.wiggleSort([4,5,5,6]))
print(a.wiggleSort([2,1]))
print(a.wiggleSort([5,3,1,2,6,7,8,5,5]))
class Solution(object):
    def search1(self, nums, target):
        """
        假设按照升序排序的数组在预先未知的某个点上进行了旋转。
        ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
        搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
        你可以假设数组中不存在重复的元素。
        你的算法时间复杂度必须是 O(log n) 级别。
        ---
        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4
        --
        输入: nums = [4,5,6,7,0,1,2], target = 3
        输出: -1
        --
        思路:
        二分查找法
        因为是两个 递增序列叠加
        分别在不同递增序列用二分查找法
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:  # <=不确定
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search(self, nums, target: int) -> int:
        if not nums: return -1
        n = len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        t = left
        print("分割点", t)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            realmid = (mid + t) % n
            print("mid", mid)
            print("realmid", realmid)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


a = Solution()
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
# print(a.search(nums = [3,1], target = 1))

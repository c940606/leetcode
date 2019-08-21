# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        left = 0
        right = mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            # left_val = M.get(left)
            mid_val = mountain_arr.get(mid)
            right_mid_val = mountain_arr.get(mid + 1)
            if mid_val > right_mid_val:
                right = mid
            else:
                left = mid + 1
        # print(left)
        loc = left
        if loc == - 1:
            loc = 0

        def helper1(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                # left_val = M.get(left)
                # right_val = mountain_arr.get(right)
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if mid_val < target:
                    left = mid + 1
                if mid_val > target:
                    right = mid - 1
            return -1

        def helper2(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                # left_val = M.get(left)
                # right_val = mountain_arr.get(right)
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if mid_val > target:
                    left = mid + 1
                if mid_val < target:
                    right = mid - 1
            return -1

        res1 = helper1(0, loc)
        if res1 != -1:
            return res1
        res2 = helper2(loc, mountain_arr.length() - 1)
        if res2 != -1:
            return res2
        return -1


a = Solution()
print(a.findInMountainArray(1, 1))

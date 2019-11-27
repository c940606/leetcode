from typing import List


class Solution:
    def countRangeSum1(self, nums: List[int], lower: int, upper: int) -> int:
        import bisect
        sort_arr = [0]
        cur = 0
        res = 0
        for num in nums:
            cur += num
            left = cur - upper
            right = cur - lower
            left_loc = bisect.bisect_left(sort_arr, left)

            if left_loc >= len(sort_arr):
                bisect.insort_left(sort_arr, cur)
                continue
            # right_loc = bisect.bisect_right(sort_arr, right)
            # if right_loc >= len(sort_arr):
            #     res += (right_loc - left_loc)
            #     bisect.insort_left(sort_arr, cur)
            # elif sort_arr[right_loc] == right:
            #     res += (right_loc - left_loc + 1)
            #     bisect.insort_left(sort_arr, cur)
            # else:
            #     res += (right_loc - left_loc)
            #     bisect.insort_left(sort_arr, cur)

            ## 方法二
            right_loc = bisect.bisect_left(sort_arr, right + 1) - 1
        return res

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        import bisect
        sort_arr = [0]
        cur = 0
        res = 0
        for num in nums:
            cur += num
            left = cur - upper
            right = cur - lower
            left_loc = bisect.bisect_left(sort_arr, left)
            right_loc = bisect.bisect_left(sort_arr, right + 1) - 1
            if left_loc >= len(sort_arr):
                bisect.insort_left(sort_arr, cur)
                continue
            res += (right_loc - left_loc + 1)
            bisect.insort_left(sort_arr, cur)
        return res


a = Solution()
print(a.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2, ))

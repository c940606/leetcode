from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        left = 0
        right = sum(time)

        def check(mid):
            n = len(time)
            days = 0
            cur = 0
            cur_max = 0
            for i in range(n):
                cur_max = max(cur_max, time[i])
                cur += time[i]
                if cur - cur_max > mid:
                    cur = time[i]
                    cur_max = time[i]
                    days += 1
            if cur > 0: days += 1
            return days <= m
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left





a = Solution()
print(a.minTime(time = [1,2,3,3,5], m = 2))
# a = Solution()
print(a.minTime(time = [999,999,999], m = 4))
print(a.minTime([1, 2, 10, 9, 8, 7, 6, 5, 9, 10], 5))

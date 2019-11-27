from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        def check(mid):
            cnt = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    cnt += 1
                    cur = weight
                else:
                    cur += weight
            #print(mid, cnt)
            return not cnt <= D
        # print(check(14))
        # print(check(15))
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
print(a.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D=5))
print(a.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], D=3))
print(a.shipWithinDays(weights=[1, 2, 3, 1, 1], D=4))

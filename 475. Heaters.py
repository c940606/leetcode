from typing import List


class Solution:
    def findRadius1(self, houses: List[int], heaters: List[int]) -> int:

        left = 0
        right = 10 ** 9
        houses.sort()
        heaters.sort()

        def check(mid):
            i = 0
            for h in heaters:
                while i < len(houses) and h - mid <= houses[i] <= h + mid:
                    i += 1
            return i == len(houses)

        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left

    def findRadius2(self, houses: List[int], heaters: List[int]) -> int:
        import bisect
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        res = 0
        for house in houses:
            loc = bisect.bisect_left(heaters, house)
            res = max(res, min(house - heaters[loc - 1], heaters[loc] - house))
        return res

    def findRadius3(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        i = 0
        res = 0
        for house in houses:
            while i < len(heaters) - 1 and house > heaters[i]:
                i += 1
            res = max(res, min(heaters[i] - house, house - heaters[i - 1]))
        return res


a = Solution()
print(a.findRadius3([1, 2, 3], [2]))
# print(a.findRadius([], []))

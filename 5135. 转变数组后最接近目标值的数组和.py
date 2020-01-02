from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        def cal(mid):
            ans = 0
            for a in arr:
                if a < mid:
                    ans += a
                else:
                    ans += mid
            return ans

        left = target // len(arr)
        right = max(arr)
        while left < right:
            # print(left, right)
            mid = (left + right) // 2
            if cal(mid) < target:
                left = mid + 1
            else:
                right = mid


        if cal(left) == target or abs(cal(left) - target) < abs(cal(left - 1) - target): # or
            #print("dfaf")
            return left
        return left - 1


a = Solution()
# print(a.findBestValue(arr=[4, 9, 3], target=10))
# print(a.findBestValue(arr=[2, 3, 5], target=10))
# print(a.findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803))
print(a.findBestValue([1547, 83230, 57084, 93444, 70879], 71237))  # 17422

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        nums_loc = []
        for idx, num in enumerate(nums):
            nums_loc.append([num, idx])
        nums_loc.sort()
        n = len(nums)
        # print(nums_loc)
        for i in range(n):
            for j in range(i + 1, n):
                if nums_loc[j][0] - nums_loc[i][0] > t:
                    break
                if abs(nums_loc[i][1] - nums_loc[j][1]) <= k:
                    return True
        return False


a = Solution()
print(a.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
print(a.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))
print(a.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))

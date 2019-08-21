class Solution:
    def threeSumSmaller1(self, nums, target) -> int:
        res = 0
        nums.sort()
        print(nums)
        n = len(nums)
        for i in range(n - 2):
            #if nums[i] >= target: break
            for j in range(i + 1, n - 1):
                #if nums[i] + nums[j] >= target: break
                for k in range(j + 1, n):
                    #print("dfa")
                    if nums[i] + nums[j] + nums[k] >= target:
                        break
                    else:
                        print(nums[i], nums[j], nums[k])
                        res += 1
        return res

    def threeSumSmaller(self, nums, target) -> int:
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res


a = Solution()
print(a.threeSumSmaller([-2, 0, 1, 3], 2))
print(a.threeSumSmaller([-1, 1, -1, -1], -1))

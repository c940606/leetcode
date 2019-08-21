class Solution:
    def findMissingRanges(self, nums, lower, upper):
        i = lower
        nums = set(nums)
        res = []
        while i <= upper:
            while i <= upper and i in nums:
                i += 1
            if i == upper + 1: break
            left = i
            while i <= upper and i not in nums:
                i += 1
            right = i - 1
            print(left, right)
            # if left > right: return []
            if left == right:
                res.append(str(left))
            else:
                res.append(str(left) + "->" + str(right))
        return res

    def findMissingRanges1(self, nums, lower, upper):
        res = []
        l = lower
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] <= upper:
                r = nums[i]
            else:
                r = upper + 1
            if l == r:
                l += 1
            elif r > l:
                if l == r - 1:
                    res.append(str(l))
                else:
                    res.append(str(l) + "->" + str(r - 1))
                    l = r + 1
            i += 1
        return res


a = Solution()
# print(a.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(a.findMissingRanges1([-1], -1, -1))
print(a.findMissingRanges1([-1], -2, -1))

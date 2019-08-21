class Solution:
    def maxProduct1(self, nums):
        if not nums: return
        cur_pro = 1
        min_pos = 1
        max_neg = float("-inf")
        res = float("-inf")
        for num in nums:
            cur_pro *= num
            # print(cur_pro)
            if cur_pro > 0:
                res = max(res, cur_pro // min_pos)
                min_pos = min(min_pos, cur_pro)
            elif cur_pro < 0:
                if max_neg != float("-inf"):
                    res = max(res, cur_pro // max_neg)
                else:
                    res = max(res, num)
                max_neg = max(max_neg, cur_pro)
            else:
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = max(res, num)
        return res

    def maxProduct(self, nums):
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


a = Solution()

# [2,3,-2,4]
# [2,-5,-2,-4,3]
# [-2]
# [1,0,-1,2,3,-5,-2]
print(a.maxProduct([1, 0, -1, 2, 3, -5, -2]))
print(a.maxProduct([2, 3, -2, 4]))
print(a.maxProduct([2, -5, -2, -4, 3]))
print(a.maxProduct([-1, -2, -3, 0]))
print(a.maxProduct([0, -2, -3]))
print(a.maxProduct([-2]))

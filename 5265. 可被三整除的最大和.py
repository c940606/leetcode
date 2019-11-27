class Solution:
    def maxSumDivThree(self, nums) -> int:
        from collections import defaultdict
        lookup = defaultdict(list)
        for num in nums:
            lookup[num % 3].append(num)
        tmp = sum(nums)
        mod = tmp % 3
        tmp1 = 0
        tmp2 = 0
        if mod == 0:
            return tmp
        if mod == 1:
            if lookup[1]:
                tmp1 = tmp - sorted(lookup[1])[0]
            if len(lookup[2]) > 1:
                tmp2 = tmp - sorted(lookup[2])[0] - sorted(lookup[2])[1]
        if mod == 2:
            if lookup[2]:
                tmp1 = tmp - sorted(lookup[2])[0]
            if len(lookup[1]) > 1:
                tmp2 = tmp - sorted(lookup[1])[0] - sorted(lookup[1])[1]
        return max(tmp1, tmp2)


a = Solution()
print(a.maxSumDivThree([3, 6, 5, 1, 8]))
print(a.maxSumDivThree(nums=[1, 2, 3, 4, 4]))
print(a.maxSumDivThree([2, 6, 2, 2, 7]))

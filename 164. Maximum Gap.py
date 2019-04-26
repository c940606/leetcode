class Solution:
    def maximumGap(self, nums) -> int:
        import math
        min_num = float("inf")
        max_num = float("-inf")
        n = len(nums)
        #print(nums)
        if n < 2: return 0
        for num in nums:
            if min_num > num:
                min_num = num
            if max_num < num:
                max_num = num
        gap = math.ceil((max_num - min_num) / (n - 1))
        #print("gap",gap)
        min_buck = [float("inf")] * (n - 1)
        max_buck = [float("-inf")] * (n - 1)
        for num in nums:
            if num == min_num or num == max_num:
                continue
            tmp = (num - min_num) // gap
            min_buck[tmp] = min(num, min_buck[tmp])
            max_buck[tmp] = max(num, max_buck[tmp])
        #print(min_buck,max_buck)
        preNum = min_num
        res = float("-inf")
        for i in range(n - 1):
            if min_buck[i] == float("inf") and max_buck[i] == float("-inf"):
                continue
            res = max(res, min_buck[i] - preNum)
            preNum = max_buck[i]
        res = max(res, max_num - preNum)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.maximumGap([3, 6, 9, 1]))

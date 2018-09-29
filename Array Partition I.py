class Solution(object):
    def arrayPairSum(self, nums):
        """
        给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，
        使得从1 到 n 的 min(ai, bi) 总和最大
        ----
        输入: [1,4,3,2]
		输出: 4
		解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
		--
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        res =[]
        n = len(nums)
        for i in range(0,n,2):
            res.append(nums[i])
        return sum(res)

    def arrayPairSum1(self, nums):
        return sum(sorted(nums)[::2])
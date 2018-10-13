class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        给定一个正整数数组 nums。
		找出该数组内乘积小于 k 的连续的子数组的个数。
		--
		输入: nums = [10,5,2,6], k = 100
		输出: 8
		解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
		需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
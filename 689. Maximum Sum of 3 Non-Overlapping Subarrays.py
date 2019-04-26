class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        cur_max = float("-inf")
        res = []
        for i in range(n - 2 * k):
            for j in range(i + k, n - k):
                for t in range(j + k, n):
                    tmp = sum(nums[i:i + k]) + sum(nums[j:j + k]) + sum(nums[t:t + k])
                    if tmp > cur_max:
                        cur_max = tmp
                        res = [i, j, t]
        return res

    def maxSumOfThreeSubarrays1(self, nums, k):
        res = [0,0,0]
        n = len(nums)
        _sum = [0] * (n + 1)
        left_range = [0] * n
        right_range = [n - k] * n
        for i in range(1, n + 1):
            _sum[i] = _sum[i - 1] + nums[i - 1]
        left_cur_sum = _sum[k] - _sum[0]
        for i in range(k, n):
            tmp = _sum[i + 1] - _sum[i + 1 - k]
            if tmp > left_cur_sum:
                left_range[i] = i + 1 - k
                left_cur_sum = tmp
            else:
                left_range[i] = left_range[i - 1]
        # print(left_range)
        right_cur_sum = _sum[n] - _sum[n - k]
        for i in range(n - k - 1, -1, -1):
            tmp = _sum[i + k] - _sum[i]
            if tmp > right_cur_sum:
                right_range[i] = i
                right_cur_sum = tmp
            else:
                right_range[i] = right_range[i + 1]
        # print(right_range)
        cur_all_sum = float("-inf")
        for i in range(k, n - 2 * k + 1):
            left = left_range[i - 1]
            right = right_range[i + k]
            tmp = (_sum[i + k] - _sum[i]) + (_sum[left + k] - _sum[left]) + (_sum[right + k] - _sum[right])
            if tmp > cur_all_sum:
                cur_all_sum = tmp
                res = [left, i, right]
        return res


a = Solution()
print(a.maxSumOfThreeSubarrays1([1, 2, 1, 2, 6, 7, 5, 1], 2))

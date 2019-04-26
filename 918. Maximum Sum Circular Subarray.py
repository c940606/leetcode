class Solution:
    def maxSubarraySumCircular(self, A):

        if not A:
            return 0
        # 记录前i最最小值
        dp = []
        cur_min_sum = 0
        all_sum = 0
        res = float("-inf")
        for a in A:
            all_sum += a
            res = max(res, all_sum - cur_min_sum)
            cur_min_sum = min(cur_min_sum, all_sum)
            dp.append(all_sum)
        # print(all_sum, cur_min_sum, dp)
        n = len(dp)
        suffix = [0] * n
        suffix[-1] = dp[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], dp[i])
        # print(suffix)
        for idx, a in enumerate(A):
            all_sum += a
            res = max(res, all_sum - suffix[idx])
            cur_min_sum = min(cur_min_sum, all_sum)
        return res

    def maxSubarraySumCircular1(self, A):
        if not A:
            return 0
        min_sum = float("-inf")
        cur_min_sum = 0
        cur_max_sum = 0
        all_sum = 0
        res_max = float("-inf")
        res_min = float("inf")
        for a in A:
            all_sum += a
            res_max = max(res_max, all_sum - cur_min_sum)
            cur_min_sum = min(all_sum, cur_min_sum)
            res_min = min(res_min, all_sum - cur_max_sum)
            cur_max_sum = max(cur_max_sum, all_sum)
        print(res_min,res_max,all_sum)
        return max(res_max, all_sum - res_min) if res_max > 0 else res_max


a = Solution()
# print(a.maxSubarraySumCircular1([1, -2, 3, -2]))
# print(a.maxSubarraySumCircular1([5, -3, 5]))
# print(a.maxSubarraySumCircular1([3, -1, 2, -1]))
# print(a.maxSubarraySumCircular1([1]))
print(a.maxSubarraySumCircular1([-2,-3,-1]))

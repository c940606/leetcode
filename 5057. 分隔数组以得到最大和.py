class Solution:
    def maxSumAfterPartitioning(self, A, K):
        import heapq
        n = len(A)
        # res = [-1] * n
        max_K = list(heapq.nlargest(K, set(A)))
        max_K_loc = list(map(A.index, max_K))
        max_K_loc_set = set(max_K_loc)
        print(max_K, max_K_loc)
        res = 0
        # print(max_K_loc_set)
        for max_num, max_loc in zip(max_K, max_K_loc):
            # print(max_K_loc_set)
            left = max_loc
            right = max_loc
            #print(max_num, max_loc)
            while left > 0 and left - 1 not in max_K_loc_set:
                left -= 1
                max_K_loc_set.add(left)
            while right < n - 1 and right + 1 not in max_K_loc_set:
                right += 1
                max_K_loc_set.add(right)
            # print(left, right, max_num)
            res += (right - left + 1) * max_num
        return res


a = Solution()
print(a.maxSumAfterPartitioning(A=[1, 15, 7, 9, 2, 5, 10], K=3))
print(a.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        from collections import defaultdict
        import bisect
        n = len(A)
        lookup = defaultdict(list)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for idx, val in enumerate(A):
            lookup[val].append(idx)

        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff]
                target = A[j] - diff
                dp[i][diff] += bisect.bisect_left(lookup[target], j)
                # for idx in lookup[target]:
                #     if idx < j:
                #         dp[i][diff] += 1
                #     else:
                #         break
            for val in dp[i].values():
                res += val
        # print(dp)

        return res
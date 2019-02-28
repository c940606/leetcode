class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':

        days = set(days)
        dp = [0] * 366

        for i in range(1, 366):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[365]

a = Solution()
print(a.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
print(a.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))

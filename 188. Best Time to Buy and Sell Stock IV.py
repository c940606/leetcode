class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[k][i][s] 在第k次交易第i天 手里有股票(s = 1)或者手里没有股票(s = 0)最大值


class Solution:
    def minFallingPathSum(self, arr) -> int:
        dp = arr[0]
        if len(dp) == 1: return dp[0]
        tmp = sorted(dp)
        num1 = tmp[0]
        num2 = tmp[1]
        for i in range(1, len(arr)):
            tmp = dp.copy()
            nxt_num1 = float("inf")
            nxt_num2 = float("inf")
            for j in range(len(arr[0])):
                if tmp[j] == num1:
                    tmp[j] = num2 + arr[i][j]
                else:
                    tmp[j] = num1 + arr[i][j]
                # 找最小两个值
                if tmp[j] < nxt_num1:
                    nxt_num2 = nxt_num1
                    nxt_num1 = tmp[j]
                elif tmp[j] < nxt_num2:
                    nxt_num2 = tmp[j]
            num1 = nxt_num1
            num2 = nxt_num2
            dp = tmp
        return min(dp)


a = Solution()
print(a.minFallingPathSum(arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(a.minFallingPathSum([[-73, 61, 43, -48, -36], [3, 30, 27, 57, 10], [96, -76, 84, 59, -15], [5, -49, 76, 31, -7],
                           [97, 91, 61, -46, 67]]))

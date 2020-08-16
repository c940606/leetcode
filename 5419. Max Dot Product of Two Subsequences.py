from typing import List


class Solution:
    def maxDotProduct1(self, nums1: List[int], nums2: List[int]) -> int:
        import functools
        n1, n2 = len(nums1), len(nums2)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == n1 or j == n2:
                return 0
            res = float("-inf")
            res = max(res, nums1[i] * nums2[j] + dfs(i + 1, j + 1), nums1[i] * nums2[j])
            if i < n1 - 1 and j < n2 - 1:
                res = max(res, dfs(i + 1, j + 1))
            if i < n1 - 1:
                res = max(res, dfs(i + 1, j))
            if j < n2 - 1:
                res = max(res, dfs(i, j + 1))
            return res

        return dfs(0, 0)

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[float("-inf")] * (n2 + 1) for _ in range(n1 + 1)]

        dp[0][0] = 0
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


a = Solution()
print(a.maxDotProduct([-5, -1, -2],
                      [3, 3, 5]))
print(a.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]))
print(a.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))
print(a.maxDotProduct([-3, -8, 3, -10, 1, 3, 9], [9, 2, 3, 7, -9, 1, -8, 5, -1, -1]))
print(a.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]))
print(a.maxDotProduct(
    [-41, 6, 29, 50, -40, -67, -49, -19, -51, 93, 5, -12, -24, 51, -33, -29, -89, 26, -7, -75, -65, 19, 57, 51, 61, -96,
     -87, -12, -16, -49, -93, -96, 72, 92, 41, -76, 99, 56, -43, 16, -73, 19, -1, -7, -71, -68, -6, -82, 76, -3, -58,
     42, 91, 8, 23, 87, 81, -37, 87, 98, 39, -40, 61, 36, -63, -70, 72, 100, -22, -52, -52, 93, 37, -76, -80, 59, 46,
     -52, 90, 6, -93, 95, -29, -79, 51, -44, -40, 99, 8, 53, -51, -41, 44, 30, -29, -97]
    ,
    [-44, -66, 50, -86, -96, 40, -70, -69, -52, -3, 59, -84, 97, 31, 9, -78, 5, -44, 63, -68, 82, 46, -82, 61, -80, -82,
     -67, -60, 52, 96, 96, 70, 49, -71, 98, -61, 68, -31, 72, -67, -1, 74, -25, 76, -86, 90, 27, 36, -49, -63, -83, -24,
     80, -31, 88, 48, -87, -14, 82, -65, -100, -71, 47, 35, -43, -85, -86, 62, 85, 80, -71, 9, -30, -55, -79, -79, 29,
     15, -7, 23, 39, 21, -45, -84, 25, 97, 57, 8, 3, 83, 32, -64, 1, 92, -44, 80, 34, -89, -16, 50]))

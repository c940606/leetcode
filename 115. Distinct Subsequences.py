class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        self.res = 0

        def backtracking(idx, t_idx):
            if t_idx == n2:
                self.res += 1
                return
            for i in range(idx, n1):
                if s[i] == t[t_idx]:
                    # print(i,t_idx)
                    backtracking(i + 1, t_idx + 1)

        backtracking(0, 0)
        return self.res

    def numDistinct1(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[1] * (n1 + 1)] + [[0] * (n1 + 1) for _ in range(n2)]
        #print(dp)

        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]


a = Solution()
print(a.numDistinct1("acdabefbc", "ab"))
print(a.numDistinct1(s="rabbbit", t="rabbit"))
# print(a.numDistinct(s="babgbag", t="bag"))
# print(a.numDistinct(
#     "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
#     "bddabdcae"))

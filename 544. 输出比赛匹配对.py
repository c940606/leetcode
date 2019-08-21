class Solution:
    def findContestMatch(self, n: int) -> str:
        team = [str(i) for i in range(1, n + 1)]

        def helper(n):
            if n == 1: return
            for i in range(n//2):
                team[i] = "(" + team[i] + "," + team[n - i - 1] + ")"

            #print(team)
            helper(n // 2)

        helper(n)
        return team[0]


a = Solution()
print(a.findContestMatch(8))

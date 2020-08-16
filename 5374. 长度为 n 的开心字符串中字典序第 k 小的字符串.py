class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        res = []

        def dfs(cur, n):

            if n == 0:
                res.append(cur)
                return
            for v in ["a", "b", "c"]:
                if cur and cur[-1] == v:continue
                dfs(cur + v, n - 1)

        dfs("", n)
        res.sort()
        if len(res) < k: return ""
        return res[k - 1]

a = Solution()
print(a.getHappyString(10, 100))
print(a.getHappyString(1, 3))
print(a.getHappyString(3, 9))


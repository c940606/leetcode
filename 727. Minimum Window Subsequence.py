class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)

        def check(s, t):
            left = 0
            for a in t:
                loc = s.find(a,left)
                if loc == -1:
                    return False
                left = loc + 1
            return True

        tmp = ""
        res = "#" * (n + 1)
        for i in range(n):
            tmp += S[i]
            while check(tmp, T):
                if len(res) > len(tmp):
                    res = tmp
                tmp = tmp[1:]
        if len(res) == n + 1: return ""
        return res


a = Solution()
print(a.minWindow("abcdebdde", T="bde"))
print(a.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "l"))

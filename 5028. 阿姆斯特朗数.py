class Solution:
    def isArmstrong(self, N: int) -> bool:
        N_str = str(N)
        n = len(N_str)
        res = 0
        for s in N_str:
            res += (int(s) ** n)
        return res == N


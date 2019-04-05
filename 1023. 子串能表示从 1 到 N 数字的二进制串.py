class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N+1):
            b = bin(i)[2:]
            if b not in S:
                return False
        return True
a = Solution()
print(a.queryString(S = "0110", N = 3))
print(a.queryString(S = "0110", N = 4))
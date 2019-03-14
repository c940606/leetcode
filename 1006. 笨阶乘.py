class Solution:
    def clumsy(self, N: int):
        res = ""
        t = ["*", "//", "+", "-"]
        j = 0
        for i in range(N, 0, -1):
            res += str(i)
            if i == 1:
                break
            res += t[j]
            j += 1
            if j == 4:
                j = 0
        # print(eval(res))
        return eval(res)

    def clumsy1(self, N: int):
        if N == 0: return 0
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        if N == 4: return 7
        return N * (N - 1) // (N - 2) + N - 3 + self.helper(N - 4)
    def helper(self,N):
        if N == 0: return 0
        if N == 1: return -1
        if N == 2: return -2
        if N == 3: return -6
        if N == 4: return -5
        return -N*(N-1)//(N-2) + N - 3 + self.helper(N-4)


a = Solution()
# print(a.clumsy(4))
print(a.clumsy1(4))

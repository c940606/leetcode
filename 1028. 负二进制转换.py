class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []

        while N:
            # res.append(str(N & 1))
            # N = -(N >> 1)
            N, b = divmod(N, 2)
            N = -N
            res.append(str(b))
        return "".join(res[::-1]) or "0"

    def baseNeg2re(self, N):
        if N == 0 or N == 1: return str(N)
        return self.baseNeg2re(-(N >> 1)) + str(N & 1)

    def base2(self, N):
        res = []

        while N:
            N, b = divmod(N, 2)
            res.append(str(b))
        # print(res)
        return "".join((res[::-1])) or "0"

    def base2re(self, N):
        if N == 0 or N == 1:
            return str(N)
        return self.base2re(N >> 1) + str(N & 1)


a = Solution()
print(a.base2re(8))
print(a.baseNeg2(3))

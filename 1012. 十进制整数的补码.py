class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n = bin(N)[2:]
        res = []
        for i in n:
            if i == "1":
                res.append("0")
            else:
                res.append("1")
        return int("".join(res),2)

    def bitwiseComplement1(self, N: int) -> int:
        X = 1
        while X < N:
            X = X<<1
            X += 1
            #print(X)
        return X - N
a = Solution()
print(a.bitwiseComplement1(5))

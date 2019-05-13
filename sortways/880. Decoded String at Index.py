class Solution:
    def decodeAtIndex(self, S: str, K) -> str:
        N = 0
        for i in range(len(S)):
            N = N * int(S[i]) if S[i].isdigit() else N + 1

            if N >= K:
                break
        for j in range(i, -1, -1):
            tmp = S[j]
            if tmp.isdigit():
                N //= int(tmp)
                K %= N
            else:
                if K == 0 or K == N: return tmp
                N -= 1


a = Solution()
print(a.decodeAtIndex(S="leet2code3", K=10))

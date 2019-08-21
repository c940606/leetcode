class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n = len(S)
        if n < K:return 0

        res = set()
        for i in range(0, n - K + 1):
            tmp = S[i:i+K]
            if len(tmp) == len(set(tmp)):
                res.add(tmp)
        return len(res)

a = Solution()
print(a.numKLenSubstrNoRepeats(S = "havefunonleetcode", K = 5))
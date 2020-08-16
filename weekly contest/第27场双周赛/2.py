class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        visited = set()
        for i in range(0, len(s) - k + 1):
            visited.add(s[i:i + k])
        return len(visited) == 2 ** k


a = Solution()
print(a.hasAllCodes(s="00110110", k=2))
print(a.hasAllCodes(s = "0000000001011100", k = 4))

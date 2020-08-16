class Solution:
    def nearestPalindromic(self, n: str) -> str:

        candidateSet = []
        l = len(str(n))
        candidateSet.append(str(10**(l-1) - 1))
        candidateSet.append(str(10**(l) + 1))
        # print(candidateSet)
        prefix = int(str(n)[:(l + 1)//2])
        for num in [prefix - 1, prefix, prefix + 1]:
            if  l % 2 == 0:
                candidateSet.append(str(num) + str(num)[::-1])
            else:
                candidateSet.append(str(num) + str(num)[:-1][::-1])
        # print(candidateSet)
        res = None
        for candidate in candidateSet:
            if candidate.startswith("00"): continue
            if res is None:
                if candidate != n:
                    res = candidate
            else:
                if candidate != n and (abs(int(candidate) - int(n)) < abs(int(res) - int(n)) or (abs(int(candidate) - int(n)) == abs(int(res) - int(n)) and int(res) > int(candidate))):
                    res = candidate
        return res
a = Solution()
print(a.nearestPalindromic("1000"))
# print(12932, 99800, 12120)
print(a.nearestPalindromic("12932"))
print(a.nearestPalindromic("1986281891"))
print(a.nearestPalindromic("1"))
print(a.nearestPalindromic("12"))
print(a.nearestPalindromic("2"))
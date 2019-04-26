class Solution:
    def confusingNumber(self, N: int) -> bool:
        lookup = {
            "1":"1",
            "0":"0",
            "6":"9",
            "8":"8",
            "9":"6"
        }
        N_str = str(N)
        t = ""
        for alp in N_str:
            if alp in lookup:
                t += lookup[alp]
            else:
                return False
        return N != int(t[::-1])

a = Solution()
print(a.confusingNumber(6))
print(a.confusingNumber(25))
print(a.confusingNumber(916))
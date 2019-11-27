class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # L R
        l = 0
        r = 0
        res = 0
        for a in s:
            if a == "L":
                l += 1
            if a == "R":
                r += 1
            if r == l:
                res += 1
                l = 0
                r = 0
        return res


a = Solution()
print(a.balancedStringSplit("RLRRLLRLRL"))
print(a.balancedStringSplit("RLLLLRRRLR"))
print(a.balancedStringSplit("LLLLRRRR"))
print(a.balancedStringSplit("RRRRRL"))
print(a.balancedStringSplit("R"))
print(a.balancedStringSplit("RRLRRLRLLLRL"))

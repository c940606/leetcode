class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if not s: return 0
        cost = []
        for x, y in zip(s, t):
            cost.append(abs(ord(y) - ord(x)))
        #print(cost)
        cur = 0
        res = 0
        left = 0
        for idx, c in enumerate(cost):
            cur += c
            while cur > maxCost:
                cur -= cost[left]
                left += 1
            res = max(res, idx - left + 1)
        return res


a = Solution()
print(a.equalSubstring("abcd", "bcdf", 3))
print(a.equalSubstring("abcd", "acde",  0))
print(a.equalSubstring("abcd", "cdef",  3))
print(a.equalSubstring("", "", 0))
print(a.equalSubstring("tyiraojpcfuttwblehv","stbtakjkampohttraky",119))
print(a.equalSubstring("krrgw","zjxss",19))
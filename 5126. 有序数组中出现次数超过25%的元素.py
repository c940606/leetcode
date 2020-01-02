class Solution:
    def findSpecialInteger(self, arr) -> int:
        from collections import Counter
        return max(Counter(arr).items(), key=lambda x:x[1])[0]

a = Solution()
print(a.findSpecialInteger([1,2,2,6,6,6,6,7,10]))

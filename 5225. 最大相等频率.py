class Solution:
    def maxEqualFreq(self, nums) -> int:

        from collections import Counter
        n = len(nums)
        c = Counter(nums)
        #print(c)
        for idx, num in enumerate(nums[::-1], 0):
            c_val = c.values()
            tmp = [t for t in c_val if t != 0]
            print(tmp)
            t  = Counter(tmp)
            if len(set(t)) == 1 and tmp[0] == 1:
                return n - idx
            if len(set(t)) == 2 and( (max(tmp) - min(tmp) == 1 and (len([t  for t in tmp if t == max(tmp) ]) == 1)) or t[1] == 1):

                return n - idx
            else:
                c[num] -= 1
        return 0

a = Solution()
print(a.maxEqualFreq( [2,2,1,1,5,3,3,5]))
# print(a.maxEqualFreq( [1,1,1,2,2,2,3,3,3,4,4,4,5]))
# print(a.maxEqualFreq([1,1,1,2,2,2]))
# print(a.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))
print(a.maxEqualFreq([1, 2]))
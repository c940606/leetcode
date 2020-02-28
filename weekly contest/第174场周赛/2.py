from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        n = len(arr)
        d = [item[1] for item in c.items()]
        d.sort(reverse=True)
        res = 1
        num = d[0]
        i = 1
        # print(d, num, n)
        while num < n // 2:
            res += 1
            num += d[i]
            i += 1
        return res
a = Solution()
print(a.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(a.minSetSize([7,7,7,7,7,7]))
print(a.minSetSize( [1,2,3,4,5,6,7,8,9,10]))
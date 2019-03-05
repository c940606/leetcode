class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        from collections import defaultdict
        num = list(str(num))
        lookup = defaultdict(lambda: -1)
        for idx, val in enumerate(num):
            lookup[val] = idx
        print(lookup)
        for idx,val in enumerate(num):
            flag = False
            for t in range(9, -1, -1):
                if t > int(val) and lookup[str(t)] > idx:
                    num[lookup[str(t)]], num[idx] = num[idx], num[lookup[str(t)]]
                    flag = True
                    break
            if flag:
                break
        return int("".join(num))
from collections import defaultdict


a = Solution()
print(a.maximumSwap(2736))
print(a.maximumSwap(9973))
print(a.maximumSwap(10))
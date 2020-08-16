from typing import List
import collections

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) <= k: return max(arr)

        cur = 0
        while 1:
            # print(arr)
            if arr[0] > arr[1]:
                cur += 1
                arr.append(arr.pop(1))
            else:
                cur = 1
                arr.append(arr.pop(0))
            if cur == k:
                return arr[0]
            
a = Solution()
print(a.getWinner(arr = [2,1,3,5,4,6,7], k = 2))

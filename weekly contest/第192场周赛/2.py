from typing import List
import collections






class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arr = sorted(arr)
        n = len(arr)
        m = sorted_arr[(n - 1)//2]
        
        return sorted(arr, key=lambda x :[abs(x - m), x], reverse=True)[:k]
    

a = Solution()
print(a.getStrongest(arr = [1,2,3,4,5], k = 2))
    
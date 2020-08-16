from typing import List
import collections

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for x, y in zip(startTime, endTime):
            if x <= queryTime <= y:
                res += 1
        return res
    
a = Solution()
print(a.busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
print(a.busyStudent(startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7))
print(a.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
from typing import List
from collections import defaultdict, deque

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        return abs((  datetime.datetime(*[int(s) for s in date2.split("-")]) - datetime.datetime(*[int(s) for s in date1.split("-")])).days)

a = Solution()
print(a.daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))
print(a.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))
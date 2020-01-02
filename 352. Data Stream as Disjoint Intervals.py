import bisect
from typing import List

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []

    def addNum(self, val: int) -> None:
        loc = bisect.bisect_left(self.res, [val])
        if loc < len(self.res):
            if self.res[loc][0] == val:
                return
            if self.res[loc][0] > val:
                if loc >= 1:
                    if self.res[loc - 1][1] >= val :
                        return
                    if self.res[loc - 1][1] + 1 == val and self.res[loc][0] - 1 == val:
                        self.res[loc - 1:loc + 1] = [[self.res[loc - 1][0], self.res[loc][1]]]
                    elif self.res[loc - 1][1] + 1 == val:
                        self.res[loc-1:loc] = [[self.res[loc-1][0], val]]
                    elif self.res[loc][0] - 1 == val:
                        self.res[loc:loc+1] = [[val, self.res[loc][1]]]
                    else:
                        if self.res[loc][0] - 1 == val:
                            self.res[loc:loc+1] = [[val, self.res[loc][1]]]
                        else:
                            self.res.insert(loc, [val, val])
                else:
                    self.res.insert(loc, [val, val])
        else:
            if self.res[loc - 1][1] >= val:
                return
            elif self.res[loc - 1][1] + 1 == val:
                self.res[loc - 1:loc] = [[self.res[loc - 1][0], val]]
            else:
                self.res.insert(loc, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
a  = SummaryRanges()
a.addNum(1)
print(a.res)
a.addNum(3)
print(a.res)
a.addNum(7)
print(a.res)
a.addNum(2)
a.addNum(6)
print(a.getIntervals())
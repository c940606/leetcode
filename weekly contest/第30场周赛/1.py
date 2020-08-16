from typing import List
import collections


class Solution:
    def reformatDate(self, date: str) -> str:
        a, b, c = date.split()
        res = []
        res.append(c)
        mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for idx, num in enumerate(mon, 1):
            if b.startswith(num):
               res.append(str(idx).ljust(2, "0"))

        tmp = ""
        for t in a:
            if t.isdigit():
                tmp += t
            else:
                break
        res.append(tmp)
        return "-".join(res)


from itertools import combinations
from typing import List


class Solution:
    def readBinaryWatch1(self, num: int) -> List[str]:
        from itertools import combinations
        res = []

        for i in range(num + 1):
            hous = []
            for item in combinations(range(4), i):
                tmp = ["0", "0", "0", "0"]
                for idx in item:
                    tmp[idx] = "1"
                # print(tmp)
                h = int("".join(tmp), 2)
                if 0 <= h <= 11:
                    hous.append(h)
            # print("hours", hous)

            # print("j", j)
            minute = []
            for item in combinations(range(7), num - i):
                # print(item)
                tmp = ["0", "0", "0", "0", "0", "0", "0"]
                for idx in item:
                    tmp[idx] = "1"
                # print(tmp)
                m = int("".join(tmp), 2)
                if 0 <= m <= 59:
                    minute.append(m)
            # print("minute", minute)
            for x in hous:
                for y in minute:
                    res.append([x, y])

        def tuple_to_str(t):
            if 0 <= t[1] < 10:
                t[1] = "0" + str(t[1])
            else:
                t[1] = str(t[1])
            t[0] = str(t[0])
            return ":".join(t)

        return [tuple_to_str(t) for t in res]

    def readBinaryWatch(self, num: int) -> List[str]:

        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == num:
                    # print(h, m)
                    res.append("{}:{:02d}".format(h, m))
        return res


a = Solution()
print(a.readBinaryWatch(1))
print(a.readBinaryWatch(2))

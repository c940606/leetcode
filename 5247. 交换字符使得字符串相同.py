class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        from collections import Counter
        c1 = Counter(s1)
        c2 = Counter(s2)
        c = c1 + c2
        if c["x"] % 2 == 1 or c["y"] % 2 == 1:
            return -1

        tmp1 = 0
        tmp2 = 0
        for a, b in zip(s1, s2):
            if a != b:
                if a == "x":
                    tmp1 += 1
                else:
                    tmp2 += 1
        return tmp1 // 2 + (tmp1 % 2) + tmp2 // 2 + (tmp2 % 2)


a = Solution()
# print(a.minimumSwap(s1="xx", s2="yy"))
# print(a.minimumSwap(s1="xy", s2="yx"))
print(a.minimumSwap(s1="xxyyxyxyxx", s2="xyyxyxxxyx"))

class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        res = ""
        flag = True
        while c:
            tmp = "".join(sorted(c.keys()))
            copy_c = c.copy()
            for k in c.keys():
                copy_c[k] -= 1
                if copy_c[k] == 0:
                    copy_c.pop(k)
            if flag:
                res += tmp
            else:
                res += tmp[::-1]
            flag = not flag
            c = copy_c
        return res
a = Solution()
print(a.sortString("aaaabbbbcccc"))
print(a.sortString(s = "rat"))


print(a.sortString(s = "leetcode"))
print(a.sortString(s = "spo"))
print(a.sortString("gggg"))
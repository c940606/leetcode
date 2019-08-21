class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from itertools import groupby
        from collections import Counter
        # 记录连续字符串的个数
        successive_char= [[k, len(list(g))] for k, g in groupby(text)]
        cnt = Counter(text)
        # print(success_num, cnt)
        res = max(min(cnt[k], c + 1) for k, c in successive_char)
        for i in range(1, len(successive_char) - 1):
            if successive_char[i - 1][0] == successive_char[i + 1][0] and successive_char[i][1] == 1:
                res = max(res, min(successive_char[i - 1][1] + successive_char[i + 1][1] + 1, cnt[successive_char[i - 1][0]]))
        return res


a = Solution()
# print(a.maxRepOpt1("ababa"))
print(a.maxRepOpt1("aaabaaa"))
# print(a.maxRepOpt1("aaaaa"))
# print(a.maxRepOpt1("aaabbaaa"))
# print(a.maxRepOpt1("aaabaaa"))

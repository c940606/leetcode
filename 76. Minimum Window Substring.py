class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import  defaultdict,Counter
        lookup = defaultdict(int)
        l_win = 0
        win = ""
        res = ""
        res_n = float("inf")
        n = len(s)
        t = Counter(t)
        for i in range(n):
            lookup[s[i]] += 1
            win += s[i]
            l_win += 1
            while all(map(lambda x:lookup[x] >= t[x],t.keys())):
                if res_n > l_win:
                    res = win
                    res_n = l_win
                lookup[win[0]] -= 1
                win = win[1:]
                l_win -= 1
        return res
a = Solution()
print(a.minWindow("ADOBECODEBANC", "ABC"))
print(a.minWindow("a","aa"))




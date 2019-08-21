class Solution:
    def minWindow3(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict, Counter
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
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if res_n > l_win:
                    res = win
                    res_n = l_win
                lookup[win[0]] -= 1
                win = win[1:]
                l_win -= 1
        return res

    def minWindow1(self, s: 'str', t: 'str') -> 'str':
        lookup = {}
        for c in s:
            lookup.setdefault(c, 0)

        for c in t:
            if c not in lookup:
                return ""
            else:
                lookup[c] += 1

        diff = len(t)
        start = 0
        end = 0
        d = float("inf")
        head = 0
        while end < len(s):
            print(start, end, diff, lookup)
            if lookup[s[end]] > 0:
                diff -= 1
            lookup[s[end]] -= 1
            end += 1
            while diff == 0:
                if end - start < d:
                    d = end - start
                    head = start
                lookup[s[start]] += 1
                if lookup[s[start]] > 0:
                    diff += 1
                start += 1

        return s[head:head + d] if d != float("inf") else ""

    def minWindow2(self, s: 'str', t: 'str') -> 'str':
        lookup = {}
        for c in s:
            lookup.setdefault(c, 0)
        s_lookup = lookup.copy()
        for c in t:
            if c not in lookup:
                return ""
            else:
                lookup[c] += 1
        start = 0
        res = ""
        for end in range(len(s)):
            while start < end and s_lookup == lookup:
                if len(res) > end - start:
                    res = s[start:end]

    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1

        return res


a = Solution()
print(a.minWindow("ADOBECODEBANC", "ABC"))
# print(a.minWindow("a", "aa"))

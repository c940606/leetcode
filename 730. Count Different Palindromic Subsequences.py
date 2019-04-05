class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        from collections import defaultdict
        import bisect
        M = 1000000007
        characters = defaultdict(list)
        for idx, s in enumerate(S):
            characters[s].append(idx)
        print(characters)
        lookup = {}

        def helper(i, j):
            if i >= j: return 0
            if (i, j) in lookup:
                return lookup[(i, j)]
            res = 0
            for c, v in characters.items():
                print(c, v)
                n = len(v)
                new_i = None
                idx_i = bisect.bisect_left(v, i)
                if idx_i < n:
                    new_i = v[idx_i]
                if new_i == None or new_i >= j:
                    continue
                idx_j = bisect.bisect_left(v, j) - 1
                new_j = v[idx_j]
                res += helper(new_i + 1, new_j) + 2 if new_i != new_j else 1
            lookup[(i, j)] = res % M
            # print(lookup)
            return lookup[(i, j)]

        return helper(0, len(S))


a = Solution()
# print(a.countPalindromicSubsequences("ab"))
print(a.countPalindromicSubsequences("bccb"))
# print(a.countPalindromicSubsequences(
#     "dfjkadfkajdfijajejraeefjijafjoiaiorjaodsjdfkjakjdfkjoejfkjadkfjoiqefdfadfwefqwefedfqwefqefqe"))

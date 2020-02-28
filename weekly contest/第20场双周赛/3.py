class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        from collections import defaultdict
        left = 0
        right = 0
        cur  = defaultdict(int)
        res = 0
        n = len(s)
        for right, val in enumerate(s):
            cur[val] += 1
            while left < right and len(cur) == 3:
                res += n - right
                cur[s[left]] -= 1
                if cur[s[left]] == 0:
                    cur.pop(s[left])
                left += 1
        return res
        # #print(left, right, cur, res)
        # while left < right:
        #     cur[s[left]] -= 1
        #     if cur[s[left]] == 0:
        #         cur.pop(s[left])
        #     if len(cur) == 3:
        #         res += 1
        #         left += 1
        #     else:
        #         break
        # return res





a = Solution()
print(a.numberOfSubstrings("abcabc"))
print(a.numberOfSubstrings("abca"))
print(a.numberOfSubstrings("aaacb"))
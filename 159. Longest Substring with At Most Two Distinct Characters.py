class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s : return 0
        left = 0
        res = float("-inf")
        for i in range(len(s)):
            while len(set(s[left:i+1])) > 2:
                left += 1
            res = max(res, i - left + 1)
        return res

    def lengthOfLongestSubstringTwoDistinct1(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] == 0:
                counter += 1
            lookup[s[end]] += 1
            end +=1
            while counter > 2:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
a = Solution()
print(a.lengthOfLongestSubstringTwoDistinct1("eceba"))
print(a.lengthOfLongestSubstringTwoDistinct1("ccaabbb"))



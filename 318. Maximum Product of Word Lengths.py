from typing import List


class Solution:

    def maxProduct1(self, words: List[str]) -> int:
        values = [0] * len(words)
        # 用位运算表示一个单词
        for i in range(len(words)):
            for alp in words[i]:
                values[i] |= 1 << (ord(alp) - 97)
        return max([len(words[i]) * len(words[j]) for i in range(len(words)) for j in range(1, len(words)) if
                    not values[i] & values[j]] or [0])

    def maxProduct(self, words: List[str]) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        for i in range(len(words)):
            mask = 0
            for alp in words[i]:
                mask |= 1 << (ord(alp) - 97)
            lookup[mask] = max(lookup[mask], len(words[i]))
        #print(lookup)
        return max([lookup[x] * lookup[y] for x in lookup for y in lookup if not x & y] or [0])


a = Solution()
print(a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(a.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))

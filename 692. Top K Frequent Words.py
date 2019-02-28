class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        from collections import Counter
        c = Counter(words)
        c = sorted(c.items(),key = lambda x:(-x[1],x[0]))
        res = []
        for i in range(k):
            res.append(c[i][0])
        return res


a = Solution()
print(a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
print(a.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))

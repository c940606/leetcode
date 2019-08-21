class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        from collections import defaultdict
        if len(words1) != len(words2): return False
        lookup = defaultdict(set)
        for x, y in pairs:
            lookup[x].add(y)
            lookup[y].add(x)
        for a, b in zip(words1, words2):
            if a == b: continue
            if b not in lookup[a] or a not in lookup[b]:
                return False
        return True

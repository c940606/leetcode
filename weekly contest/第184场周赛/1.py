from typing import List


class Solution:
    def stringMatching1(self, words: List[str]) -> List[str]:
        res = set()
        for w1 in words:
            for w2 in words:
                if w1 == w2: continue
                if len(w1) > len(w2) and w1.find(w2) != -1:
                    res.add(w2)
        return list(res)

    def stringMatching(self, words: List[str]) -> List[str]:

        trie = {}

        def add(word):
            cur = trie
            for w in word:
                cur = cur.setdefault(w, {})

        def get(word):
            cur = trie
            for w in word:
                if (cur := cur.get(w)) is None:
                    return False
            return True

        words.sort(key=len, reverse=True)
        res = []
        for word in words:
            if get(word): res.append(word)
            for i in range(len(word)):
                add(word[i:])
        return res


a = Solution()
print(a.stringMatching(["mass", "as", "hero", "superhero"]))
print(a.stringMatching(["leetcode", "et", "code"]))
print(a.stringMatching(["blue", "green", "bu"]))
print(a.stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"]))

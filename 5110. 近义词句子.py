from typing import List
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        f = {}
        all_words = set()
        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(x)] = find(y)

        for x, y in synonyms:
            union(x, y)
            all_words.add(x)
            all_words.add(y)

        text = text.split()
        words = all_words & set(text)
        from collections import defaultdict
        g = defaultdict(list)
        for word in words:
            tmp = find(word)
            for item in all_words:
                if tmp == find(item):
                    g[word].append(item)

        res = []
        def dfs(i, tmp):
            if i == len(text):
                res.append(" ".join(tmp))
                return
            if text[i] in words:
                for item in g[text[i]]:
                    dfs(i + 1, tmp + [item])
            else:
                dfs(i + 1, tmp + [text[i]])
        dfs(0, [])
        return sorted(res)

a  = Solution()
print(a.generateSentences(synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],text = "I am happy today but was sad yesterday"))
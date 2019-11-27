from pprint import pprint


class Solution:
    def findNumOfValidWords1(self, words, puzzles):
        from collections import defaultdict
        trie = defaultdict(int)
        for word in words:
            cur = trie
            for w in sorted(set(word)):
                cur.setdefault(w, defaultdict(int))
                cur = cur[w]
            cur["end"] += 1

        # print(trie)

        def helper(trie, puzzle, firstSeen, firstLetter):
            # print(puzzle, trie)
            if not trie: return 0
            c = 0
            if firstSeen:
                c += trie["end"]
            for p in puzzle:
                if p == firstLetter:
                    c += helper(trie[p], puzzle, True, firstLetter)
                else:
                    c += helper(trie[p], puzzle, firstSeen, firstLetter)
            return c

        res = []
        for idx, puzzle in enumerate(puzzles):
            tmp = helper(trie, sorted(puzzle), False, puzzle[0])
            res.append(tmp)
        return res

    def findNumOfValidWords(self, words, puzzles):
        from collections import Counter
        from itertools import product, compress
        c = Counter(["".join(sorted(set(word))) for word in words])
        res = [0] * len(puzzles)
        for idx, puzzle in enumerate(puzzles):
            for t in product([0, 1], repeat=len(puzzle) - 1):
                p = compress(puzzle, [1] + list(t))
                res[idx] += c["".join(sorted(p))]
        return res


a = Solution()
print(a.findNumOfValidWords(words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                            puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
# print(a.findNumOfValidWords(["a", "aaa", "aa"], []))
# print(a.findNumOfValidWords())

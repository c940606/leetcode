from collections import deque


class Solution(object):
    def minMutation1(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        bank = set(bank)
        if end not in bank:
            return -1
        visited = set()
        visited.add(start)
        mutation = {"A", "C", "G", "T"}

        def oneMutation(cur):
            for i, val in enumerate(cur):
                for t in mutation - {val}:
                    tmp = cur[:i] + t + cur[i + 1:]
                    if tmp in bank:
                        yield tmp

        queue = deque()
        queue.appendleft([start, 0])
        while queue:
            cur, res = queue.pop()
            if cur == end:
                return res
            for nxt in oneMutation(cur):
                visited.add(nxt)
                queue.appendleft((nxt, res + 1))
        return -1

    def minMutation(self, start, end, bank):
        bank = set(bank)

        if end not in bank:
            return -1
        visited = set()
        visited.add(start)
        mutation = {"A", "C", "G", "T"}

        def honeMutation(cur):
            for i, val in enumerate(cur):
                for t in mutation - {val}:
                    tmp = cur[:i] + t + cur[i + 1:]
                    if tmp in bank:
                        yield tmp

        def bfs(s):
            if s == end:
                return 0
            res = float("inf")
            for nxt in honeMutation(s):
                if nxt not in visited:
                    visited.add(nxt)
                    res = min(res, 1 + bfs(nxt))
                    visited.remove(nxt)
            return res

        tmp = bfs(start)
        return tmp if tmp != float("inf") else -1


a = Solution()
print(a.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(a.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(a.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))
print(a.minMutation("AAAAAAAA", "CCCCCCCC",
                    ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC",
                     "CCCCCCCA", "CCCCCCCC"]))
print(a.minMutation("AAAACCCC", "CCCCCCCC",
                    ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]))


# "TAUXX TAUXX TAUXX TAUXX TAUXX"
# "TAUXX TAUXX TAUXX TAUXX TAUXX TAUXX TAUXX TAUXX TAUXX"
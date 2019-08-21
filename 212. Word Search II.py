class Solution(object):
    def findWords1(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = []
        if not board: return res
        row = len(board)
        col = len(board[0])

        def helper(word, i, j, visited):
            visited.add((i, j))
            if not word:
                return True
            for x, y in dirs:
                tmp_i, tmp_j = i + x, j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and board[tmp_i][tmp_j] == \
                        word[0]:
                    if helper(word[1:], tmp_i, tmp_j, visited):
                        return True
            visited.remove((i, j))
            return False

        lookup = defaultdict(list)
        for i in range(row):
            for j in range(col):
                lookup[board[i][j]].append((i, j))

        for word in set(words):
            if word[0] in lookup:
                for x, y in lookup[word[0]]:
                    if helper(word[1:], x, y, set()):
                        res.append(word)
                        break

        return res

    def findWords(self, board, words):
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1
        res = []
        row = len(board)
        col = len(board[0])
        def dfs(i, j, trie, s):
            c = board[i][j]
            if c not in trie: return
            trie = trie[c]
            s += c
            if "end" in trie and trie["end"] == 1:
                res.append(s)
                trie["end"] = 0
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s)
            board[i][j] = c
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res

a = Solution()
print(a.findWords(words=["oath", "pea", "eat", "rain"], board=
[
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
                  ))
print(a.findWords(
    [["a"]]
    , ["a", "a"]))
print(a.findWords([["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
                   ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
                   ["a", "a", "b", "a", "a", "b"]],
                  [
                      "bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
                      "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
                      "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
                      "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
                      "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
                      "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
                      "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
                      "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
                      "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
                      "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]))

from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        lookup = {}
        res = []
        for word in words:
            cur = lookup
            for w in word:
                cur.setdefault(w, {})
                cur = cur[w]
            cur["#"] = "#"

        # print(lookup)
        # 寻找有prefix前缀长度为l的单词
        def helper(prefix, l):
            ans = []
            cur = lookup
            for p in prefix:
                if p not in cur:
                    return ans
                cur = cur[p]

            def dfs(prefix, cur):
                if "#" in cur and len(prefix) == l:
                    ans.append(prefix)
                    return
                if len(prefix) > l:
                    return

                for b in cur:
                    if b != "#":
                        dfs(prefix + b, cur[b])

            dfs(prefix, cur)
            return ans

        def backtrack(tmp, _len):
            # 数组里个数
            tmp_len = len(tmp)
            if tmp_len == _len:
                res.append(tmp)
                return
            # 目前列表的前缀
            prefix = ""
            for t in tmp:
                prefix += t[tmp_len]
            for nxt in helper(prefix, _len):
                backtrack(tmp + [nxt], _len)

        for word in words:
            backtrack([word], len(word))
        return res


a = Solution()
print(a.wordSquares(["area", "lead", "wall", "lady", "ball"]))
print(a.wordSquares(["abat", "baba", "atan", "atal"]))

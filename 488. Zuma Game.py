class Solution:
    def findMinStep1(self, board: str, hand: str) -> int:
        """
        枚举插入位置, 消除


        :param board:
        :param hand:
        :return:
        """
        from itertools import groupby
        import functools
        def helper(tmp):
            while 1:
                cmp_s = tmp
                cur = ""
                for k, item in groupby(tmp):
                    n = len(list(item))
                    if n > 2: continue
                    cur += k * n
                if cmp_s == cur: break
                tmp = cur
            return cur

        @functools.lru_cache(None)
        def dfs(b, h):
            # print(b, h)
            if not b:
                return 0
            if not h:
                return float("inf")
            res = float("inf")
            for i in range(len(b) + 1):
                for j in range(len(h)):
                    tmp = b[:i] + h[j] + b[i:]
                    tmp = helper(tmp)
                    res = min(res, 1 + dfs(tmp, h[:j] + h[j + 1:]))
            return res

        res = dfs(board, hand)
        return -1 if res == float("inf") else res

    def findMinStep(self, board: str, hand: str) -> int:
        from itertools import groupby
        from collections import Counter
        cnt = Counter(hand)

        def dfs(board):
            if not board:
                return 0
            res = float("inf")
            cur_loc = 0
            for k, item in groupby(board):
                n = len(list(item))
                need = max(3 - n, 0)
                if cnt[k] >= need:
                    cnt[k] -= need
                    res = min(res, need + dfs(board[:cur_loc] + board[cur_loc + n:]))
                    cnt[k] += need
                cur_loc += n
            return res

        return -1 if (res := dfs(board)) == float("inf") else res


a = Solution()
# print(a.findMinStep("WRRBBW", "RB"))
# print(a.findMinStep("WWRRBBWW", "WRBRW"))
# print(a.findMinStep("RBYYBBRRB", "YRBGB"))
# print(a.findMinStep("G", "GGGGG"))
# print(a.findMinStep("R"*20, "G"*5))
print(a.findMinStep("RRWWRRBBR",
"WB"))

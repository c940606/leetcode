from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        from collections import defaultdict
        person = defaultdict(int)
        for x, y, z in transactions:
            person[x] -= z
            person[y] += z
        accounts = []
        for v in person.values():
            accounts.append(v)
        res = float("inf")

        def dfs(i, cnt):
            nonlocal res
            if cnt >= res: return
            while i < len(accounts) and accounts[i] == 0: i += 1
            if i == len(accounts):
                res = min(res, cnt)
                return
            for j in range(i + 1, len(accounts)):
                if accounts[i] * accounts[j] < 0:
                    accounts[j] += accounts[i]
                    dfs(i + 1, cnt + 1)
                    accounts[j] -= accounts[i]

        dfs(0, 0)
        return res


a = Solution()
print(a.minTransfers([[0, 1, 10], [2, 0, 5]]))
print(a.minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))
print(a.minTransfers([[0, 1, 1], [1, 2, 1], [2, 0, 1]]))

from typing import List


class Solution:
    def minFlips1(self, mat: List[List[int]]) -> int:
        from collections import deque
        row = len(mat)
        col = len(mat[0])
        status = []
        for i in range(row):
            for j in range(col):
                status.append(mat[i][j])

        queue = deque([tuple(status)])
        visited = set([tuple(status)])
        res = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                # print(tmp)
                if len(set(tmp)) == 1 and tmp[0] == 0:
                    return res

                for i in range(row * col):
                    t = list(tmp)
                    t[i] ^= 1
                    if i - col >= 0:
                        t[i - col] ^= 1
                    if i + col < len(tmp):
                        t[i + col] ^= 1
                    if i + 1 < len(tmp) and (i + 1) % col != 0:
                        t[i + 1] ^= 1
                    if i % col != 0 and i - 1 >= 0:
                        t[i - 1] ^= 1
                    if tuple(t) not in visited:
                        queue.appendleft(tuple(t))
                        visited.add(tuple(t))
            res += 1
        return -1

    def minFlips(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        n = row * col

        def check(bit):
            for i in range(row):
                for j in range(col):
                    _sum = mat[i][j]
                    for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1], [0, 0]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col:
                            loc = tmp_i * col + tmp_j
                            if bit & (1 << loc) != 0:
                                _sum += 1
                    if _sum % 2 != 0: return float("inf")
            return cal(bit)

        def cal(bit):
            return sum(1 if bit & (1 << i) != 0 else 0 for i in range(1 << n))

        res = min(check(i) for i in range(1 << n))

        return res if res != float("inf") else -1


a = Solution()
print(a.minFlips([[0, 0], [0, 1]]))
print(a.minFlips([[1, 1, 1], [1, 0, 1], [0, 0, 0]]))
print(a.minFlips(mat=[[1, 0, 0], [1, 0, 0]]))
print(a.minFlips([[1]]))

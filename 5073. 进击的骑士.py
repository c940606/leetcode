class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        from collections import deque
        queue = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        step = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                i, j = queue.pop()
                if i == x and j == y:
                    return step
                for s, t in [[-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, 2], [2, 1], [1, -2], [2, -1]]:
                    tmp_i = s + i
                    tmp_j = t + j
                    if -300 <= tmp_i <= 300 and -300 <= tmp_j <= 300 and (tmp_i, tmp_j) not in visited:
                        visited.add((tmp_i, tmp_j))
                        queue.appendleft((tmp_i, tmp_j))

            step += 1


a = Solution()
# print(a.minKnightMoves(x=2, y=1))
# print(a.minKnightMoves(x=5, y=5))
# print(a.minKnightMoves(2, 112))
# print(a.minKnightMoves(-27, -166))
# print(a.minKnightMoves(11, 248))
# print(a.minKnightMoves(114,-179))
# print(a.minKnightMoves(-172,-110))
# print(a.minKnightMoves(-99, 142))
# print(a.minKnightMoves(-34,-156))
# print(a.minKnightMoves(-84,170))
# print(a.minKnightMoves(68,-157))
# print(a.minKnightMoves(209,-58))
# print(a.minKnightMoves(-33,92))
# print(a.minKnightMoves(136,-63))
# print(a.minKnightMoves(-16,-42))
# print(a.minKnightMoves(157,-42))
# print(a.minKnightMoves(97,133))
# print(a.minKnightMoves(-35,211))
# print(a.minKnightMoves(-76,144))
# print(a.minKnightMoves(52,-99))
# print(a.minKnightMoves(-87,83))
# print(a.minKnightMoves(-45,-102))
# print(a.minKnightMoves(-35,211))
# print(a.minKnightMoves(300,0))
# print(a.minKnightMoves(22,163))
print(a.minKnightMoves(0,-300))
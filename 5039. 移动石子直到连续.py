class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        # if b <= a or c <= b:
        #     return [0, 0]
        res = [0, 0]
        a, b, c = sorted([a, b, c])
        #print(a, b, c)
        b_a = b - a
        c_b = c - b
        if b_a == 1 and c_b == 1:
            res[0] = 0
        elif b_a == 1 or c_b == 1:
            res[0] = 1
        elif b_a == 2 or c_b == 2:
            res[0] = 1
        else:
            res[0] = 2
        res[1] = b_a - 1 + c_b - 1

        return res


a = Solution()
# print(a.numMovesStones(a=1, b=2, c=5))
# print(a.numMovesStones(2, 4, 1))
print(a.numMovesStones(4, 3, 2))
# print(a.numMovesStones(3, 5, 1))  # [1,2]

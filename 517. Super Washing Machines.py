class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        target, b = divmod(sum(machines), n)
        if b != 0: return -1


        moves = [0] * n
        res = 0
        for i in range(n - 1):
            if target < machines[i]:
                machines[i] = target
                moves[i] = machines[i] - target
                machines[i + 1] += machines[i] - target
                res = max(res, moves[i])
            else:
                machines[i] = target
                machines[i + 1] -= target - machines[i]
                moves[i + 1] += target - machines[i]
                res = max(res, moves[i - 1] )

        return res

import heapq
from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.lookup = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.lookup[playerId] += score

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.lookup.values()))

    def reset(self, playerId: int) -> None:
        self.lookup.pop(playerId)

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

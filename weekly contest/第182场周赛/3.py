import collections


class UndergroundSystem:

    def __init__(self):
        self._id = collections.defaultdict(list)
        self.time = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._id[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.time[(self._id[id][0], stationName)].append(t - self._id[id][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.time[(startStation, endStation)]) / len(self.time[(startStation, endStation)])

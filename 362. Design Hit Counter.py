from collections import deque, defaultdict


class HitCounter1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = deque()
        self.lookup = defaultdict(int)
        self.now = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # print(self.lookup, self.time)
        while self.time and timestamp - self.time[-1] + 1 > 300:
            self.lookup.pop(self.time.pop())
        if timestamp > self.now:
            self.time.appendleft(timestamp)
            self.now = timestamp
        self.lookup[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.time and timestamp - self.time[-1] + 1 > 300:
            self.lookup.pop(self.time.pop())
        return sum(self.lookup.values())


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and timestamp - self.queue[-1] + 1 > 300:
            self.queue.pop()
        return len(self.queue)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

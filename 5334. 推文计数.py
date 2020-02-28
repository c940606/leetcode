
class TweetCounts:

    def __init__(self):
        from collections import defaultdict
        self.lookup = defaultdict(list)
        self.f = {
            "minute" : 60,
            "hour": 3600,
            "day": 86400
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.lookup[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        res = [0 for _ in range(startTime, endTime + 1, self.f[freq])]
        for tmp in self.lookup[tweetName]:
            res[(tmp - startTime)//(self.f[freq])] += 1
        return res





# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

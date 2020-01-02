from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeline = defaultdict(list)
        self.userId_follower = defaultdict(set)
        self.now = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.timeline[userId].append((self.now, tweetId))
        self.now += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        for uid in self.userId_follower[userId] | {userId}:
            for tmp in self.timeline[uid]:
                res.append(tmp)
        res.sort(reverse=True)
        return [tw for _, tw in res[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.userId_follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """

        self.userId_follower[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

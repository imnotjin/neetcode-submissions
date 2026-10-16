import collections
import heapq

class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.user_tweets = collections.defaultdict(list) # userId -> list of (timestamp, tweetId)
        self.following = collections.defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        max_heap = []

        # Include self in the target users
        followees = self.following[userId] | {userId}

        # Push the most recent tweet from each followee into the heap
        for followeeId in followees:
            tweets = self.user_tweets[followeeId]
            if tweets:
                last_idx = len(tweets) - 1
                time, tweetId = tweets[last_idx]
                # Max-heap: store negative timestamp
                max_heap.append((-time, tweetId, followeeId, last_idx - 1))

        heapq.heapify(max_heap)

        # k-way merge to get up to 10 recent tweets
        while max_heap and len(res) < 10:
            neg_time, tweetId, followeeId, next_idx = heapq.heappop(max_heap)
            res.append(tweetId)
            if next_idx >= 0:
                next_time, next_tweetId = self.user_tweets[followeeId][next_idx]
                heapq.heappush(max_heap, (-next_time, next_tweetId, followeeId, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
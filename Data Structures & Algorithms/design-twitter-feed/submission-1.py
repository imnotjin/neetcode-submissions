class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        m = self.tweet_map
        m[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        followees = self.follow_map[userId] | {userId}

        for f_id in followees:
            tweets = self.tweet_map[f_id]
            if tweets:
                last_idx = len(tweets) - 1
                time, t_id = tweets[last_idx]
                max_heap.append((-time, t_id, f_id, last_idx - 1))
        heapq.heapify(max_heap)

        while max_heap and len(res) < 10:
            neg_time, t_id, f_id, nxt_idx = heapq.heappop(max_heap)
            res.append(t_id)
            if nxt_idx >= 0:
                nxt_time, nxt_tid = self.tweet_map[f_id][nxt_idx]
                heapq.heappush(max_heap, (-nxt_time, nxt_tid, f_id, nxt_idx - 1))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        m = self.follow_map
        m[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        m = self.follow_map
        m[followerId].discard(followeeId)


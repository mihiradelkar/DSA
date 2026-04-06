class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followers[userId] | {userId}
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets)-1
                time, tweetId = tweets[idx]
                heapq.heappush(heap,(-time,tweetId,uid,idx-1))
        
        res = []
        while heap and len(res)<10:
            _,tweetId,uid,idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx>=0:
                time, nextTweetId = self.tweets[uid][idx]
                heapq.heappush(heap,(-time,nextTweetId,uid,idx-1))
        return res 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
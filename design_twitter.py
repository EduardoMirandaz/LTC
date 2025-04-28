
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.posts = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append(
            [userId, tweetId]
        )

    def getNewsFeed(self, userId: int) -> list[int]:
        

        followers_ids = self.users[userId]

        last_10_tweets = []

        for post in self.posts[::-1]:
            if len(last_10_tweets) >= 10: return last_10_tweets 
            if post[0] in followers_ids or post[0] == userId:
                last_10_tweets.append(post[1])

        return last_10_tweets
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].remove(followeeId)

twitter = Twitter()
print(twitter.postTweet(1, 5)) # User 1 posts a new tweet (id = 5).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
print(twitter.follow(1, 2))    # User 1 follows user 2.
print(twitter.postTweet(2, 6)) # User 2 posts a new tweet (id = 6).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
print(twitter.unfollow(1, 2))  # User 1 unfollows user 2.
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
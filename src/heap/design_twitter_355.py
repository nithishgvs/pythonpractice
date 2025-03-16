import heapq
from collections import defaultdict
from typing import List


class Twitter:
    user_follower_map = {}
    user_tweets = {}
    time = 0

    def __init__(self):
        self.user_follower_map = defaultdict(set)
        self.user_tweets = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].add((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        for tweet in self.user_tweets[userId]:
            all_tweets.append(tweet)
        for follows in self.user_follower_map[userId]:
            for tweet in self.user_tweets[follows]:
                all_tweets.append(tweet)
        top_n = 10 if len(all_tweets) >= 10 else len(all_tweets)
        result = [tweetId for _, tweetId in heapq.nlargest(top_n, all_tweets)]
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.user_follower_map[followerId]:
            self.user_follower_map[followerId].remove(followeeId)


def test_twitter():
    twitter = Twitter()
    twitter.postTweet(2, 5);  # User 1 posts a new tweet (id = 5).
    #twitter.getNewsFeed(1);  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2);  # User 1 follows user 2.
    twitter.follow(1, 2);  # User 1 follows user 2.
    #twitter.postTweet(2, 6);  # User 2 posts a new tweet (id = 6).
    twitter.getNewsFeed(
        1);  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    #twitter.unfollow(1, 2);  # User 1 unfollows user 2.
    #twitter.getNewsFeed(
        #1);  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (26.86%)
# Total Accepted:    31.9K
# Total Submissions: 118.8K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
# 
# 
# 
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# 
# 
# 
# Example:
# 
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
# 
# 
#
class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.flow_manager = {}
        self.user_tweet_manager = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if self.has(self.user_tweet_manager, userId):
            self.user_tweet_manager[userId].append((tweetId, self.time))
        else:
            self.user_tweet_manager[userId] =[(tweetId, self.time)]
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        user_history = []
        if self.has(self.user_tweet_manager, userId):
            user_history = self.user_tweet_manager[userId][-10:]
        others = []
        if self.has(self.flow_manager, userId):
            followees = self.flow_manager.get(userId, [])
            for i in range(len(followees)):
                others.extend(self.user_tweet_manager.get(followees[i], [])[-10:])
        others.extend(user_history)
        print(others)
        others.sort(key=lambda x: x[1], reverse=True)
        l = 10 if len(others) > 10 else len(others)
        return [others[i][0] for i in range(l)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if self.has(self.flow_manager, followerId):
            if followeeId in self.flow_manager[followerId]:
                pass
            else:
                self.flow_manager[followerId].append(followeeId)
        else:
            self.flow_manager[followerId] = [followeeId]
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        followes = self.flow_manager.get(followerId, [])
        if followeeId in followes:
            followes.remove(followeeId)
    
    def has(self, dict, key):
        return dict.__contains__(key)



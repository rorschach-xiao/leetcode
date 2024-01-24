import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.id2followees = {}
        self.id2tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.id2tweets:
            self.id2tweets[userId] = [(self.timestamp, tweetId)]
        else:
            self.id2tweets[userId].append((self.timestamp, tweetId))
        if len(self.id2tweets) > 10:
            self.id2tweets[userId].pop(0)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.id2followees:
            followees = list(self.id2followees[userId])
            users = [userId] + followees
        else:
            users = [userId]
        heap = []
        # add latest tweet of current user to heap
        for i, user in enumerate(users):
            if user in self.id2tweets:
                heapq.heappush(heap, (-self.id2tweets[user][-1][0],
                                      self.id2tweets[user][-1][1],
                                      i,
                                      len(self.id2tweets[user]) - 1))

        j = 0
        ans = []
        while j < 10 and len(heap) > 0:
            time, tId, uId, k = heapq.heappop(heap)
            ans.append(tId)
            if k > 0:
                heapq.heappush(heap, (-self.id2tweets[users[uId]][k - 1][0],
                                      self.id2tweets[users[uId]][k - 1][1],
                                      uId,
                                      k - 1))
            j += 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.id2followees:
            self.id2followees[followerId] = set([followeeId])
        else:
            self.id2followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.id2followees:
            self.id2followees[followerId].remove(followeeId)
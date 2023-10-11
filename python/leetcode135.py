from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        numOfCandies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                numOfCandies[i] = numOfCandies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                numOfCandies[i] = max(numOfCandies[i + 1] + 1, numOfCandies[i])
        return sum(numOfCandies)
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = [c - maxCandies + extraCandies >= 0 for c in candies]
        return res
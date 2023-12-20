from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainderMap = {}
        for t in time:
            remainder = t % 60
            if remainder not in remainderMap:
                remainderMap[remainder] = 1
            else:
                remainderMap[remainder] += 1
        ans = 0
        for t in time:
            remainder = t % 60
            if remainder < 30 and 60 - remainder in remainderMap:
                ans += remainderMap[60 - remainder]
        if 30 in remainderMap and remainderMap[30] > 1:
            ans += (remainderMap[30] * (remainderMap[30] - 1)) // 2
        if 0 in remainderMap and remainderMap[0] > 1:
            ans += (remainderMap[0] * (remainderMap[0] - 1)) // 2
        return ans
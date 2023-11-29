from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        re = 0
        preSum = 0
        for g in gain:
            preSum += g
            if preSum > re:
                re = preSum
        return re
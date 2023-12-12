from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre1, pre2 = 0, 0
        for i in range(2, n + 1):
            cur = min(pre1 + cost[i - 1], pre2 + cost[i - 2])
            pre2 = pre1
            pre1 = cur
        return cur
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        s, l, n = days[0], days[-1], len(days)
        dp = {}
        dp[l] = min(costs)
        j1, j7, j30 = n - 1, n - 1, n - 1
        for i in range(n - 2, -1, -1):

            while days[j30] - days[i] >= 30:
                j30 -= 1
            while days[j7] - days[i] >= 7:
                j7 -= 1
            while days[j1] - days[i] >= 1:
                j1 -= 1

            cost1 = dp[days[j1 + 1]] + costs[0] if j1 + 1 < n else costs[0]
            cost7 = dp[days[j7 + 1]] + costs[1] if j7 + 1 < n else costs[1]
            cost30 = dp[days[j30 + 1]] + costs[2] if j30 + 1 < n else costs[2]
            dp[days[i]] = min(cost1, cost7, cost30)

        return dp[s]
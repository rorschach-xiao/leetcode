from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float('inf') for _ in range(n)] for _ in range(k + 2)]
        dp[0][src] = 0
        for t in range(0, k + 2):
            for flight in flights:
                if t == 0 and flight[0] == src:
                    dp[t][flight[1]] = flight[2]
                else:
                    dp[t][flight[1]] = min(dp[t][flight[1]], dp[t - 1][flight[0]] + flight[2])
        ans = float('inf')
        for i in range(k + 1):
            ans = min(ans, dp[i][dst])

        return -1 if ans == float('inf') else ans
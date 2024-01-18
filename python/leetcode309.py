from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 1:
#             return 0
#         dp = [[0 for _ in range(3)] for _ in range(n)]
#         dp[0][1] = -prices[0]
#         for i in range(1, n):
#             dp[i][0] = max(dp[i-1][0], dp[i-1][2])
#             dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
#             dp[i][2] = dp[i-1][1] + prices[i]
#         return max(dp[n-1][0], dp[n-1][2])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        # dp[i][0] 第i天 不持有股票 非cooldown
        # dp[i][1] 第i天 持有股票 非cooldown
        # dp[i][2] 第i天 不持有股票 cooldown
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[n-1][2],dp[n-1][0])

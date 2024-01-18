from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 1:
#             return 0
#         buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
#         for i in range(1, n):
#             buy1 = max(buy1, -prices[i])
#             sell1 = max(sell1, buy1 + prices[i])
#             buy2 = max(buy2, sell1 - prices[i])
#             sell2 = max(sell2, buy2 + prices[i])
#         return max(sell1, sell2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # status[0] 第一次持有股票
        # status[1] 不持有股票 完成1次交易
        # status[2] 第二次持有股票
        # status[3] 不持有股票 完成2次交易
        status = [0 for _ in range(4)]
        status[0], status[2] = -prices[0], -prices[0]
        for i in range(1, n):
            status[0] = max(status[0], -prices[i])
            status[1] = max(status[1], status[0] + prices[i])
            status[2] = max(status[2], status[1] - prices[i])
            status[3] = max(status[3], status[2] + prices[i])
        return status[3]
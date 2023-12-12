# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 1:
#             return 0
#         pre_price = None
#         inf = 10 ** 4 + 1
#         min_price = inf
#         profit = 0
#         is_own = 0
#         for price in prices:
#             if pre_price is not None:
#                 if price > pre_price and is_own == 0:
#                     is_own = 1
#                 elif price < pre_price and is_own == 1:
#                     profit += pre_price - min_price
#                     min_price = price
#                     is_own = 0
#             min_price = min(price, min_price)
#             pre_price = price
#         if is_own == 1:
#             profit += max(0, prices[-1] - min_price)
#         return profit
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        own_flag = False
        ans = 0
        for i in range(n - 1):
            # bug the stock
            if prices[i] < prices[i + 1] and not own_flag:
                own_flag = True
                ans -= prices[i]
            # sell the stock
            if prices[i] > prices[i + 1] and own_flag:
                ans += prices[i]
                own_flag = False
        if own_flag:
            ans += prices[n - 1]
        return ans

if __name__ =='__main__':
    solution = Solution()
    print(solution.maxProfit([2,4,1]))
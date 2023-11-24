from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        status = [-prices[0] if i % 2 == 0 else 0 for i in range(k * 2)]
        for i in range(n):
            for s in range(k * 2):
                if s == 0:
                    status[s] = max(status[s], -prices[i])
                elif s % 2 == 0:
                    status[s] = max(status[s], status[s-1] - prices[i])
                else:
                    status[s] = max(status[s], status[s-1] + prices[i])
        return status[-1]
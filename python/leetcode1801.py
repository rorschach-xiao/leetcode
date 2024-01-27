import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        buyHeap = []
        sellHeap = []
        res = 0
        for order in orders:
            price, amount, orderType = order
            if orderType == 0: # buy
                while sellHeap and sellHeap[0][0] <= price and amount > 0:
                    p_sell, a_sell = heapq.heappop(sellHeap)
                    if a_sell > amount:
                        a_sell -= amount
                        res -= amount
                        amount = 0
                    else:
                        amount -= a_sell
                        res -= a_sell
                        a_sell = 0
                    if a_sell:
                        heapq.heappush(sellHeap, (p_sell, a_sell))
                if amount:
                    heapq.heappush(buyHeap, (-price, amount))
                    res += amount
            else: # sell
                while buyHeap and -buyHeap[0][0] >= price and amount > 0:
                    p_buy, a_buy = heapq.heappop(buyHeap)
                    if a_buy > amount:
                        a_buy -= amount
                        res -= amount
                        amount = 0
                    else:
                        amount -= a_buy
                        res -= a_buy
                        a_buy = 0
                    if a_buy:
                        heapq.heappush(buyHeap, (p_buy, a_buy))
                if amount:
                    heapq.heappush(sellHeap, (price, amount))
                    res += amount

        return res % MOD

if __name__ == '__main__':
    solution = Solution()
    orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
    print(solution.getNumberOfBacklogOrders(orders))
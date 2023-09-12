class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        profit = 0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = max(profit, price - minPrice)
        return profit

if __name__ == '__main__':
    solution = Solution()
    prices = [7,5,2,4,7,3,1]
    print(solution.maxProfit(prices))
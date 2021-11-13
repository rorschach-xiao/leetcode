class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp_pre = 0
        dp_cur = None
        min_p = prices[0]
        for i in range(n):
            if prices[i] < min_p:
                min_p = prices[i]
            if i!=0:
                dp_cur = max(dp_pre,prices[i]-min_p)
                dp_pre = dp_cur
        if dp_cur is None:
            return 0
        else:
            return dp_cur

if __name__ == '__main__':
    solution = Solution()
    prices = [7,5,2,4,7,3,1]
    print(solution.maxProfit(prices))
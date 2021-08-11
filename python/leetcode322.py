# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#
#         coins.sort(reverse=True)
#         self.coins = coins
#         self.result = float("inf")
#         for i in range(len(self.coins)):
#             self.dfs(i,0,amount)
#         if self.result == float("inf"):
#             return -1
#         else:
#             return self.result
#
#     def dfs(self,start,cur_num,amount):
#         if amount == 0:
#             self.result = min(self.result,cur_num)
#         for i in range(start,len(self.coins)):
#             if (self.result-cur_num)*self.coins[i] <amount:
#                 break
#             if self.coins[i] > amount:
#                 continue
#             else:
#                 self.dfs(i,cur_num+1,amount-self.coins[i])

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if  i-c >= 0 :
                    dp[i] = min(dp[i-c]+1,dp[i])

        return dp[amount] if dp[amount]!= float("inf") else -1



if __name__=='__main__':
    solution = Solution()
    coins = [186, 419, 83, 408]
    # coins = [1,7,10]
    print(solution.coinChange(coins,6249))
    # print(solution.D)
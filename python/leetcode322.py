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
from typing import List


# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if amount == 0:
#             return 0
#         coins.sort(reverse=True)
#         dp = [float("inf")] * (amount+1)
#         dp[0] = 0
#         for i in range(amount+1):
#             for c in coins:
#                 if  i-c >= 0 :
#                     dp[i] = min(dp[i-c]+1,dp[i])
#
#         return dp[amount] if dp[amount]!= float("inf") else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = set(coins)
        n = len(coins)
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                for coin in coins:
                    if i - coin >= 0 and dp[i - coin] != float("inf"):
                        dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == float("inf") else dp[amount]



if __name__=='__main__':
    solution = Solution()
    coins = [1, 2, 5]
    # coins = [1,7,10]
    print(solution.coinChange(coins,100))
    # print(solution.D)
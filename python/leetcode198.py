# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         dp = [0]*n
#         result = 0
#         for i in range(n):
#             if i==0:
#                 dp[i] = nums[i]
#             elif i==1:
#                 dp[i] = max(nums[i],nums[i-1])
#             else:
#                 cur_max_money = 0
#                 for j in range(i-1):
#                     if dp[j]+nums[i] > cur_max_money:
#                         cur_max_money = dp[j]+nums[i]
#                 dp[i] = cur_max_money
#             if dp[i] >result:
#                 result = dp[i]
#         return result
from typing import List


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         prePre = nums[0]
#         pre = max(nums[1], nums[0])
#         maxRob = pre
#         for i in range(2, n):
#             cur = max(nums[i] + prePre, pre)
#             prePre = pre
#             pre = cur
#             maxRob = max(maxRob, cur)
#         return maxRob

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        prePre = 0
        pre = nums[0]
        maxMoney = float('-inf')
        for i in range(2, n + 1):
            curRob = max(pre, prePre + nums[i - 1])
            prePre = pre
            pre = curRob
            maxMoney = max(maxMoney, curRob)
        return maxMoney
if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,9,3,1]
    print(solution.rob(nums))
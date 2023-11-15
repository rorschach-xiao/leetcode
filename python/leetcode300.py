
from typing import List


# dp
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 1
#         dp = [1 for _ in range(n)]
#         maxLen = float("-inf")
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                 maxLen = max(maxLen, dp[i])
#         return maxLen

# binary search + greedy
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        tails = [nums[0]]
        for i in range(n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                left, right = 0, len(tails)
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                tails[left] = nums[i]
        return len(tails)

if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,2,3]
    print(solution.lengthOfLIS(nums))
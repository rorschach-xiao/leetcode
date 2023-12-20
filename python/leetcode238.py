# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         result = [0] * n
#         L = [0] * n
#         R = [0] * n
#         for i in range(n):
#             if i == 0:
#                 L[i] = 1
#                 R[n-1-i] = 1
#             else:
#                 L[i] = L[i-1] * nums[i - 1]
#                 R[n-1-i] = R[n-i] * nums[n-i]
#         for i in range(n):
#             result[i] = L[i] * R[i]
#         return result
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1 for _ in range(n)]
        right_prod = [1 for _ in range(n)]
        for i in range(1, n):
            left_prod[i] = nums[i - 1] * left_prod[i - 1]
            right_prod[n - i - 1] = nums[n - i] * right_prod[n - i]

        ans = []
        for i in range(n):
            ans.append(left_prod[i] * right_prod[i])
        return ans
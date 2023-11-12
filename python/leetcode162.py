# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return 0
#         left = 0
#         right = len(nums)-1
#         while(left<right):
#             mid = (left+right) // 2
#             if nums[mid] > nums[mid+1]:
#                 right = mid
#             else:
#                 left = mid+1
#         return left
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left
if __name__== '__main__':
    nums = [1,2,3,4,1,5,6]
    solution = Solution()
    print(solution.findPeakElement(nums))
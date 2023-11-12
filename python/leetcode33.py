# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         self.nums = nums
#
#         left_p = 0
#         right_p = len(nums)-1
#         return self.helper(left_p,right_p,target)
#
#
#     def helper(self,left,right,target):
#         if left>right:
#             return -1
#         mid = (left+right)//2
#         if self.nums[mid] == target:
#             return mid
#         else:
#             if self.nums[mid]>=self.nums[left]:
#                 if self.nums[mid]<target or self.nums[left]>target:
#                     return self.helper(mid+1,right,target)
#                 else:
#                     return self.helper(left,mid-1,target)
#             else:
#                 if self.nums[mid]>target or self.nums[right]<target:
#                     return self.helper(left,mid-1,target)
#                 else:
#                     return self.helper(mid+1,right,target)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] > nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] < nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    print(solution.search(nums,2))

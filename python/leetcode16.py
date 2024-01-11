# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if len(nums) == 3:
#             return sum(nums)
#         nums = sorted(nums)
#         result = None
#         last_sum = None
#         for i in range(0, len(nums) - 1):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             start = i + 1
#             end = len(nums) - 1
#             # double pointer traverse
#             while(start < end):
#                 cur_sum = nums[i] + nums[start] + nums[end]
#                 # update current sum
#                 if result is None or abs(cur_sum - target) < abs(result - target):
#                     result = cur_sum
#
#                 if cur_sum > target:
#                     end -= 1
#                     while (start < end and nums[end] == nums[end + 1]):
#                         end -= 1
#                 elif cur_sum < target:
#                     start += 1
#                     while(start < end and nums[start] == nums[start - 1]):
#                         start += 1
#                 else:
#                     return target
#         return result
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        nums = sorted(nums)
        closest_sum = None
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if not closest_sum or abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    return target
        return closest_sum


if __name__ == '__main__':
    solution = Solution()
    nums = [4,0,5,-5,3,3,0,-4,-5]
    target = -2
    print(solution.threeSumClosest(nums, target))
# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         result = []
#         if not nums or len(nums) < 4:
#             return result
#
#         sorted_nums = sorted(nums)
#         n = len(sorted_nums)
#         for i in range(n - 3):
#             if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
#                 continue
#             if target > sorted_nums[i] + sorted_nums[n - 1] + sorted_nums[n - 2] + sorted_nums[n - 3]:
#                 continue
#             if target < sorted_nums[i] + sorted_nums[i + 1] + sorted_nums[i + 2] + sorted_nums[i + 1]:
#                 break
#             current_target = target - sorted_nums[i]
#             current_results = self.__threeSum(sorted_nums[i + 1:], current_target)
#             if current_results is not None and len(current_results) > 0:
#                 for current_result in current_results:
#                     result.append([sorted_nums[i]] + current_result)
#         return result
#
#     def __threeSum(self, nums, target):
#         result = []
#         n = len(nums)
#         for i in range(n - 2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             if target > nums[i] + nums[n-1] + nums[n-2]:
#                 continue
#             if target < nums[i] + nums[i + 1] + nums[i + 2]:
#                 break
#             current_target = target - nums[i]
#             current_results = self.__twoSum(nums[i + 1:], current_target)
#             if current_results is not None and len(current_results) > 0:
#                 for current_result in current_results:
#                     result.append([nums[i]] + current_result)
#         return result
#
#     def __twoSum(self, nums, target):
#         result = []
#         n = len(nums)
#         for i in range(n - 1):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             if target > nums[i] + nums[n - 1]:
#                 continue
#             if target < nums[i] + nums[i + 1]:
#                 break
#             current_target = target - nums[i]
#             left = i + 1
#             right = len(nums) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == current_target:
#                     result.append([nums[i], nums[mid]])
#                     break
#                 elif nums[mid] > current_target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#         return result
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums = sorted(nums)
        quadSet = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur_sum < target:
                        left += 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        quadSet.add(str([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1

        return [map(int, quad[1:-1].split(',')) for quad in quadSet]

if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([-1, 0, 1, 2, -1, -4], -1))

# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         jump = 0
#         start = 0
#         end = 1
#         n = len(nums)
#         while end < n:
#             maxPos = 0
#             for i in range(start, end):
#                 if nums[i] + i > maxPos:
#                     maxPos = nums[i] + i
#             start = end
#             end = maxPos + 1
#             jump += 1
#         return jump
from typing import List


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         start, end = 0, 1
#         n = len(nums)
#         jump = 0
#         if n == 1:
#             return 0
#
#         while end < n:
#             next_end = end
#             while start < end:
#                 if start + nums[start] > next_end:
#                     next_end = nums[start] + start
#                 start += 1
#             jump += 1
#             end = next_end + 1
#
#         return jump

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        end, next_end = nums[0], nums[0]
        i, jump = 0, 1
        while end < n - 1 :
            while i <= end:
                if i + nums[i] > next_end:
                    next_end = i + nums[i]
                i += 1
            jump += 1
            end = next_end

        return jump

if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([1,2,3]))
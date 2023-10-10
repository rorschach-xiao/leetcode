# class Solution:
#     def removeDuplicates(self, nums):
#         prev = None
#         cur_ele_len = 1
#         i = 0
#         while (i < len(nums)):
#             cur = nums[i]
#             if prev is None or prev is not None and prev != cur:
#                 cur_ele_len = 1
#                 prev = cur
#                 i += 1
#             elif prev == cur and cur_ele_len < 2:
#                 cur_ele_len += 1
#                 i += 1
#             elif prev == cur and cur_ele_len >= 2:
#                 nums.pop(i)
#
#         return len(nums)
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n <= 1:
#             return n
#         left = 1
#         pre_ele = nums[0]
#         n = len(nums)
#         cur_len = 1
#         while(left < n):
#             cur_ele = nums[left]
#             if cur_ele == pre_ele:
#                 if cur_len < 2:
#                     cur_len += 1
#                     left += 1
#                 else:
#                     nums.pop(left)
#                     n -= 1
#             else:
#                 pre_ele = cur_ele
#                 cur_len = 1
#                 left += 1
#         print(nums)
#         return n
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, n = 0, len(nums)
        if n <= 2:
            return n
        current_repeat = 1
        for i in range(1, n):
            if nums[i] == nums[k]:
                current_repeat += 1
                if current_repeat <= 2:
                    k += 1
                    nums[k] = nums[i]
            else:
                k += 1
                nums[k] = nums[i]
                current_repeat = 1
        return k+1

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1,2,2,3]
    print(solution.removeDuplicates(nums))
    print(nums)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        if len(nums) == 0:
            return [start, end]

        # find start
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or (mid > 0 and nums[mid - 1] != target):
                    start = mid
                    break
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # find end
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or (mid < len(nums) - 1 and nums[mid + 1] != target):
                    end = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [start, end]
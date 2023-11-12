from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        if target > nums[right]:
            return right + 1
        if target < nums[left]:
            return 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return min(left,right) + 1
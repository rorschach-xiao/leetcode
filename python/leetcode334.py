from typing import List


class Solution:
    # greedy
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first, second = nums[0], float("inf")
        for i in range(1, len(nums)):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False

    # double pointer
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        leftMin = [0] * n
        rightMax = [0] * n
        leftMin[0] = nums[0]
        rightMax[-1] = nums[-1]

        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i])
            rightMax[n - i - 1] = max(rightMax[n - i], nums[n - i - 1])

        for i in range(1, n - 1):
            if leftMin[i - 1] < nums[i] < rightMax[i + 1]:
                return True
        return False

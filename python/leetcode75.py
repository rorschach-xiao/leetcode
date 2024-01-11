from typing import List


class Solution:

    # counting sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros, ones, twos = 0, 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        n = len(nums)
        for i in range(n):
            if i < zeros:
                nums[i] = 0
            elif i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2

    # two pointers
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p1 = 0, 0
        for i in range(n):
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    nums[p1], nums[i] = nums[i], nums[p1]

                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

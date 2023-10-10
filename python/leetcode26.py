from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, n = 0, len(nums)
        if n <= 1:
            return n
        for i in range(1, n):
            if nums[i] == nums[k]:
                continue
            else:
                k += 1
                nums[k] = nums[i]
        return k + 1
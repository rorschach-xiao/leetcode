from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        n = len(nums)
        for i in range(n):
            _dict[nums[i]] = i

        for i, num in enumerate(nums):
            if target - num in _dict and _dict[target - num] != i:
                return [i, _dict[target - num]]
        return []
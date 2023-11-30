from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        head = 0
        n = len(nums)
        maxLen = 0
        k = 1
        for i in range(n):
            if nums[i] == 0:
                k -= 1
            if k < 0:
                if nums[head] == 0:
                    k += 1
                head += 1
            maxLen = max(maxLen, i - head + 1)
        return maxLen - 1
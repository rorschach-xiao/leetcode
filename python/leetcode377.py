from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        nums = sorted(nums)
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num]
        return dp[target]
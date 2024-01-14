from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s < target or (s - target) % 2 != 0:
            return 0
        neg = (s - target) // 2
        dp = [[0 for _ in range(neg + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(neg + 1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
        return dp[n][neg]
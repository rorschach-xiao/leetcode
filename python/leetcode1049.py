from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        stone_sum = sum(stones)
        dp = [[False for _ in range(stone_sum // 2 + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(stone_sum // 2 + 1):
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i-1]]
        for j in range(stone_sum // 2, -1, -1):
            if dp[n][j]:
                return stone_sum - 2 * j
        return stone_sum
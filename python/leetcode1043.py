from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            cur_max = float('-inf')
            for l in range(1, k + 1):
                if l > i:
                    break
                cur_max = max(cur_max, arr[i - l])
                dp[i] = max(dp[i], dp[i - l] + cur_max * l)
        return dp[n]

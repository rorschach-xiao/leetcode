class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j), j * (i - j))
        return dp[n]
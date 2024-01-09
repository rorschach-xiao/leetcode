class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j * j<= i:
                dp[i] = min(dp[i],1 + dp[i - j * j])
                j += 1
        return dp[n]
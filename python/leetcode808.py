class Solution:
    def soupServings(self, n: int) -> float:
        if n % 25 != 0:
            n = n // 25 + 1
        else:
            n //= 25
        n = min(200, n)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            dp[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = 1/4 * (dp[max(0, i-4)][j]
                + dp[max(0, i-3)][j-1] + dp[max(0, i - 2)][max(0, j - 2)] + dp[i - 1][max(0, j - 3)])
        return dp[n][n]
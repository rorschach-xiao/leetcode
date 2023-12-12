class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0 for _ in range(4)] for _ in range(2)]
        dp[1][1] = dp[1][0] = 1
        for i in range(2, n + 1):
            a, b = i & 1, (i - 1) & 1
            dp[a][0] = dp[b][1]
            dp[a][1] = sum(dp[b])
            dp[a][2] = dp[b][0] + dp[b][3]
            dp[a][3] = dp[b][0] + dp[b][2]

        return dp[n & 1][1] % 1000000007
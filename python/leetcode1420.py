class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        if k == 0:
            return 0
        dp = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[1][1][j] = 1
        for i in range(2, n + 1):
            for c in range(1, k + 1):
                presum = 0
                for j in range(1, m + 1):
                    dp[i][c][j] = (dp[i - 1][c][j] * j) % MOD
                    dp[i][c][j] += presum % MOD
                    presum += dp[i - 1][c - 1][j] % MOD
        return sum(dp[n][k]) % MOD
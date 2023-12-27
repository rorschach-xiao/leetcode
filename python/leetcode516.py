class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        dp = [[1 for _ in range(n)] for _ in range(n)]
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if s[i] == s[j]:
                    if L == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
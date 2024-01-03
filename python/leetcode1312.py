class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[1 for _ in range(n)] for _ in range(n)]
        maxLen = 1
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if s[i] == s[j]:
                    if L == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                maxLen = max(maxLen, dp[i][j])
        return n - maxLen
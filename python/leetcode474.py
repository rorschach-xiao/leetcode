from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(l + 1)]
        for i in range(1, l+1):
            zeros = strs[i-1].count('0')
            ones = strs[i-1].count('1')
            for j in range(0, m+ 1):
                for k in range(0, n + 1):
                    if zeros > j or ones > k:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones] + 1)
        return dp[l][m][n]
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        minPathSum = float('inf')
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                if i == n-1:
                    minPathSum = min(minPathSum, dp[i][j])
        return minPathSum
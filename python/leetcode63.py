from typing import List


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         if obstacleGrid[0][0] == 1:
#             return 0
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = 1
#         for i in range(1, m):
#             if obstacleGrid[i][0] == 0:
#                 dp[i][0] = dp[i - 1][0]
#
#         for j in range(1, n):
#             if obstacleGrid[0][j] == 0:
#                 dp[0][j] = dp[0][j - 1]
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 if obstacleGrid[i][j] == 0:
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#
#         return dp[m - 1][n - 1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += dp[i][j-1] if j != 0 else 0
                    dp[i][j] += dp[i-1][j] if i != 0 else 0
        return dp[m-1][n-1]
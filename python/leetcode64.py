# class Solution(object):
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j>0:
#                     dp[i][j] = dp[i][j-1] + grid[i][j]
#                 elif j==0 and i>0:
#                     dp[i][j] = dp[i-1][j] + grid[i][j]
#                 elif i==0 and j == 0:
#                     dp[i][j] = grid[0][0]
#                 else:
#                     dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
#         return dp[m-1][n-1]
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        # dp initialization
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for j in range(1, m):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(solution.minPathSum(grid))
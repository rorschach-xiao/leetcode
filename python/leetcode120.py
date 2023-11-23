from typing import List

# TLE
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         self.triangle = triangle
#         self.ans = float("inf")
#         self.dfs(0, 0, 0)
#         return self.ans
#
#     def dfs(self, idx, row, pathSum):
#         if row == len(self.triangle):
#             self.ans = min(pathSum, self.ans)
#             return
#         self.dfs(idx, row + 1, pathSum + self.triangle[row][idx])
#         if idx + 1 < len(self.triangle[row]):
#             self.dfs(idx + 1, row + 1, pathSum + self.triangle[row][idx + 1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        if row == 1:
            return triangle[0][0]
        dp = [[0 for _ in range(i + 1)] for i in range(row)]
        dp[0][0] = triangle[0][0]
        ans = float("inf")
        for i in range(1, row):
            for j in range(i+1):
                if j - 1 >=0 and j < len(triangle[i - 1]):
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                elif j < len(triangle[i - 1]):
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                if i == row - 1:
                    ans = min(ans, dp[i][j])
        return ans

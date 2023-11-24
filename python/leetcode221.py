# class Solution(object):
#     def maximalSquare(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         h = len(matrix)
#         w = len(matrix[0])
#         dp = [[0 for _ in range(w)] for _ in range(h)]
#         max_len = 0
#         for i in range(h):
#             for j in range(w):
#                 if (i == 0 or j == 0) and matrix[i][j] == "1":
#                     dp[i][j] = 1
#                 else:
#                     if matrix[i][j] == "1":
#                         dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
#                 if dp[i][j] >max_len:
#                     max_len = dp[i][j]
#         max_area = max_len ** 2
#         return max_area
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxEdge = 0
        # dp initialization
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                if maxEdge == 0: maxEdge = 1

        for j in range(1, n):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                if maxEdge == 0: maxEdge = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxEdge = max(maxEdge, dp[i][j])
        return maxEdge ** 2

if __name__=='__main__':
    solution = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(solution.maximalSquare(matrix))
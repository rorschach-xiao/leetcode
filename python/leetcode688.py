class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        offsets = [[-1, -2], [-2, -1], [1, -2], [2, -1], [-1, 2], [-2, 1], [1, 2], [2, 1]]
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = 1
        for p in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for offset in offsets:
                        new_r, new_c = i + offset[0], j + offset[1]
                        if 0 <= new_r < n and 0 <= new_c < n:
                            dp[i][j][p] += dp[new_r][new_c][p - 1] / 8

        return dp[row][column][k]
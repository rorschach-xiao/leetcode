class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        h = len(dungeon)
        w = len(dungeon[0])
        # dp matrix initialization
        dp = [[1] * w for _ in range(h)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(h - 2, -1, -1):
            dp[i][w - 1] = max(dp[i + 1][w - 1] - dungeon[i][w - 1], 1)
        for i in range(w - 2, -1, -1):
            dp[h - 1][i] = max(dp[h - 1][i + 1] - dungeon[h - 1][i], 1)

        for i in range(h - 2, -1, -1):
            for j in range(w - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]), 1)

        return dp[0][0]

if __name__ == '__main__':
    solution = Solution()
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(solution.calculateMinimumHP(dungeon))
class Solution:
    def deleteGreatestValue(self, grid):
        if len(grid) == 1:
            return sum(grid)

        m = len(grid)
        n = len(grid[0])
        # sort
        for i in range(m):
            grid[i] = sorted(grid[i])

        ans = 0
        for j in range(n):
            ans += max([grid[i][j] for i in range(m)])
        return ans

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,2,4],[3,3,1]]
    print(solution.deleteGreatestValue(grid))
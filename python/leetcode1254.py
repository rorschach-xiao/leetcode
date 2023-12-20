from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.m, self.n = m, n
        self.grid = grid
        self.offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # eliminate open island
        for i in range(m):
            if self.grid[i][0] == 0:
                self.grid[i][0] = 1
                self.bfs(i, 0)
            if self.grid[i][n - 1] == 0:
                self.grid[i][n - 1] = 1
                self.bfs(i, n - 1)
        for j in range(n):
            if self.grid[0][j] == 0:
                self.grid[0][j] = 1
                self.bfs(0, j)
            if self.grid[m - 1][j] == 0:
                self.grid[m - 1][j] = 1
                self.bfs(m - 1, j)
        numOfClosedIslands = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if self.grid[i][j] == 0:
                    numOfClosedIslands += 1
                    self.bfs(i, j)
        return numOfClosedIslands

    def bfs(self, row, col):
        def isValidPos(r, c):
            return 0 <= r < self.m and 0 <= c < self.n

        queue = deque([(row, col)])
        while queue:
            cur_row, cur_col = queue.popleft()
            for offset in self.offsets:
                new_row = cur_row + offset[0]
                new_col = cur_col + offset[1]
                if isValidPos(new_row, new_col) and self.grid[new_row][new_col] == 0:
                    self.grid[new_row][new_col] = 1
                    queue.append((new_row, new_col))



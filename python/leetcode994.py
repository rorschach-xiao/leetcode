from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.numOfFresh = sum([sum([1 for i in r if i == 1]) for r in grid])
        self.time = 0
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        queue = deque()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    queue.append([i, j])
        self.bfs(queue)

        return self.time if self.numOfFresh == 0 else -1

    def bfs(self, queue):
        def isValidPos(pos):
            return 0 <= pos[0] < self.m and 0 <= pos[1] < self.n

        next_queue = deque()
        time = -1
        while queue:
            cur_pos = queue.popleft()
            self.grid[cur_pos[0]][cur_pos[1]] = 3
            for offset in self.offsets:
                new_pos = [cur_pos[0] + offset[0], cur_pos[1] + offset[1]]
                if isValidPos(new_pos) and self.grid[new_pos[0]][new_pos[1]] == 1:
                    next_queue.append(new_pos)
                    self.grid[new_pos[0]][new_pos[1]] = 3
                    self.numOfFresh -= 1
            if len(queue) == 0:
                queue = next_queue
                next_queue = deque()
                time += 1
        self.time = max(self.time, time)

if __name__ == '__main__':
    solution = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution.orangesRotting(grid)

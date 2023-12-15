from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        def isValidPos(row, col):
            return 0 <= row < m and 0 <= col < n

        k = min(m + n - 3, k)
        queue = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        step = 0
        while queue:
            l = len(queue)
            step += 1
            for _ in range(l):
                row, col, leftK = queue.popleft()
                for offset in offsets:
                    new_row = row + offset[0]
                    new_col = col + offset[1]
                    if isValidPos(new_row, new_col):
                        if grid[new_row][new_col] == 1 and leftK > 0 and (new_row, new_col, leftK - 1) not in visited:
                            visited.add((new_row, new_col, leftK - 1))
                            queue.append((new_row, new_col, leftK - 1))

                        elif grid[new_row][new_col] == 0 and (new_row, new_col, leftK) not in visited:
                            if new_row == m - 1 and new_col == n - 1:
                                return step
                            visited.add((new_row, new_col, leftK))
                            queue.append((new_row, new_col, leftK))
        return -1

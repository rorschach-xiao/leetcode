from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        row_set = {}
        col_set = {}
        for i in range(n):
            row = str(grid[i])
            col = str([row[i] for row in grid])
            if row not in row_set:
                row_set[row] = 1
            else:
                row_set[row] += 1
            if col not in col_set:
                col_set[col] = 1
            else:
                col_set[col] += 1
        for row in row_set.keys():
            if row in col_set:
                ans += row_set[row] * col_set[row]
        return ans
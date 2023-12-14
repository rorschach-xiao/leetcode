from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        ms = prefixSum2D(pizza)

        @cache
        def dfs(i, j, c):
            if c == 0:
                return 1 if ms.query(i, j, m, n) else 0
            res = 0
            for j2 in range(j + 1, n):
                if ms.query(i, j, m, j2):
                    res += dfs(i, j2, c - 1)
            for i2 in range(i + 1, m):
                if ms.query(i, j, i2, n):
                    res += dfs(i2, j, c - 1)
            return res % (10 ** 9 + 7)

        return dfs(0, 0, k - 1)


class prefixSum2D:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        s = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = matrix[i - 1][j - 1]
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (x == 'A')
        self.s = s

    def query(self, r1, c1, r2, c2):
        return self.s[r2][c2] + self.s[r1][c1] - self.s[r2][c1] - self.s[r1][c2]

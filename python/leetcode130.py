from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        self._offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self._visit = [[False for _ in range(n)] for _ in range(m)]
        self._grid = board
        # traverse the leftmost column and the rightmost column
        for i in range(m):
            if board[i][0] == "O" and not self._visit[i][0]:
                self.helper([i, 0], False)
            if board[i][n - 1] == "O" and not self._visit[i][n - 1]:
                self.helper([i, n - 1], False)

        # traverse the top row and the bottom row
        for j in range(n):
            if board[0][j] == "O" and not self._visit[0][j]:
                self.helper([0, j], False)
            if board[m - 1][j] == "O" and not self._visit[m - 1][j]:
                self.helper([m - 1, j], False)

        # traverse inner part
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O" and not self._visit[i][j]:
                    self.helper([i, j], True)

    def helper(self, pos, flip):
        def isValidPos(p):
            return 0 <= p[0] < len(self._grid) and 0 <= p[1] < len(self._grid[0])

        queue = [pos]
        while len(queue) > 0:
            cur = queue.pop(0)
            if flip:
                self._grid[cur[0]][cur[1]] = "X"
            self._visit[cur[0]][cur[1]] = True
            for offset in self._offsets:
                next_pos = [cur[0] + offset[0], cur[1] + offset[1]]
                if isValidPos(next_pos) and not self._visit[next_pos[0]][next_pos[1]] and \
                        self._grid[next_pos[0]][next_pos[1]] == "O":
                    self._visit[next_pos[0]][next_pos[1]] = True
                    queue.append(next_pos)


if __name__ == '__main__':

    solution = Solution()
    grid = [["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
    solution.solve(grid)
    print(grid)




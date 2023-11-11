from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.n = n
        self.columns = set()
        self.diag1 = set()
        self.diag2 = set()
        self.helper(0, [])
        return self.res

    def helper(self, row, queens):
        if len(queens) == self.n:
            self.res.append(self.generate_board(queens))
            return
        for col in range(self.n):
            if col in self.columns:
                continue
            if row - col in self.diag1:
                continue
            if row + col in self.diag2:
                continue

            self.columns.add(col)
            self.diag1.add(row - col)
            self.diag2.add(row + col)
            queens.append([row, col])
            self.helper(row + 1, queens)
            queens.pop()
            self.columns.remove(col)
            self.diag1.remove(row - col)
            self.diag2.remove(row + col)



    def generate_board(self, queens):
        board = [['.' for _ in range(self.n)] for _ in range(self.n)]
        for queen in queens:
            board[queen[0]][queen[1]] = 'Q'
        for i in range(self.n):
            board[i] = ''.join(board[i])
        return board



if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(5))
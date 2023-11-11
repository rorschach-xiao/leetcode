class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.n = n
        self.columns = set()
        self.diag1 = set()
        self.diag2 = set()
        self.helper(0)
        return self.res

    def helper(self, row):
        if row == self.n:
            self.res += 1
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
            self.helper(row + 1)
            self.columns.remove(col)
            self.diag1.remove(row - col)
            self.diag2.remove(row + col)

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(5))
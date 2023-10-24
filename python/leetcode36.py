from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenSet = set([])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                s = f"({board[i][j]})"
                if (s + str(i) not in seenSet and
                    str(j) + s not in seenSet and
                    str(i//3) + s + str(j//3) not in seenSet):
                    seenSet.add(s + str(i))
                    seenSet.add(str(j) + s)
                    seenSet.add(str(i//3) + s + str(j//3))
                else:
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(board))
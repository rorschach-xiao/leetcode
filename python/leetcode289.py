from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                board[i][j] = self.checkStatus(board, i, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: # 1 -> 0
                    board[i][j] = 0
                elif board[i][j] == 3: # 0 -> 1
                    board[i][j] = 1


    def checkStatus(self, board, row, col, m, n) -> int:
        current_status = board[row][col]
        neighbor_offsets = [[0, 1], [1, 0], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
        if current_status == 0:  # dead
            num_live = 0
            for offset in neighbor_offsets:
                if self.isValidPosition(row + offset[0], col + offset[1], m, n):
                    neighbor = board[row + offset[0]][col + offset[1]]
                    if neighbor == 1 or neighbor == 2:
                        num_live += 1
                if num_live > 3:
                    break
            if num_live == 3:
                return 3
            return 0

        else:  # live
            num_live = 0
            for offset in neighbor_offsets:
                if self.isValidPosition(row + offset[0], col + offset[1], m, n):
                    neighbor = board[row + offset[0]][col + offset[1]]
                    if neighbor == 1 or neighbor == 2:
                        num_live += 1
                if num_live > 3:
                    break
            if num_live == 2 or num_live == 3:
                return 1
            return 2

    def isValidPosition(self, row, col, m, n) -> bool:
        if 0 <= row < m and 0 <= col < n:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    board = [[0,1,0],
             [0,0,1],
             [1,1,1],
             [0,0,0]]
    solution.gameOfLife(board)
    print(board)
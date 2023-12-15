# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         h = len(board)
#         w = len(board[0])
#         self.h = h
#         self.w = w
#         self.board = board
#         self.offset = [[0,1],[1,0],[0,-1],[-1,0]]
#         is_visit = [[0 for _ in range(w)] for _ in range(h)]
#         for i in range(h):
#             for j in range(w):
#                 if board[i][j] == word[0]:
#                     re = self.dfs(is_visit,word[1:],(i,j))
#                     if re:
#                         return True
#         return False
#
#     def dfs(self,is_visit,cur_word,cur_pos):
#         if len(cur_word)==0:
#             return True
#         else:
#             is_visit[cur_pos[0]][cur_pos[1]] = 1
#             for _offset in self.offset:
#                 new_pos = [cur_pos[0]+_offset[0],cur_pos[1]+_offset[1]]
#                 if self.is_valid_pos(new_pos) and is_visit[new_pos[0]][new_pos[1]]== 0 and \
#                     self.board[new_pos[0]][new_pos[1]] == cur_word[0]:
#                     is_visit[new_pos[0]][new_pos[1]] = 1
#                     re = self.dfs(is_visit,cur_word[1:],new_pos)
#                     is_visit[new_pos[0]][new_pos[1]] = 0
#                     if re == True:
#                         return True
#             is_visit[cur_pos[0]][cur_pos[1]] = 0
#             return False
#
#     def is_valid_pos(self,pos):
#         if 0<=pos[0]<self.h and 0<=pos[1]<self.w:
#             return True
#         else:
#             return False

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.board = board
        self.offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.m, self.n = m, n
        self.visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.visited[i][j] = 1
                    if self.dfs(i, j, word, 1):
                        return True
                    self.visited[i][j] = 0
        return False

    def dfs(self, row, col, word, k):

        def isValidPos(r, c):
            return 0 <= r < self.m and 0 <= c < self.n

        if len(word) == k:
            return True

        result = False
        for offset in self.offsets:
            new_row = row + offset[0]
            new_col = col + offset[1]
            if isValidPos(new_row, new_col) and self.visited[new_row][new_col] == 0 and self.board[new_row][new_col] == \
                    word[k]:
                self.visited[new_row][new_col] = 1
                result = self.dfs(new_row, new_col, word, k + 1)
                if result:
                    return True
                self.visited[new_row][new_col] = 0
        return result
if __name__ =='__main__':
    solution = Solution()
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print(solution.exist(board,word))
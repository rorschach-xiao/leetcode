# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         self.m = len(matrix)
#         self.n = len(matrix[0])
#         if self.m == 0 or self.n == 0:
#             return []
#
#         self.offset_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         self.is_visit_map = [[0 for _ in range(self.n)] for _ in range(self.m)]
#         cur_coord = [0, 0]
#         cur_dir = 0
#         result = []
#         while (True):
#             result.append(matrix[cur_coord[0]][cur_coord[1]])
#             self.is_visit_map[cur_coord[0]][cur_coord[1]] = 1
#             new_coord = [self.offset_list[cur_dir][0] + cur_coord[0], self.offset_list[cur_dir][1] + cur_coord[1]]
#             if (not self.check_position_validation(new_coord)):
#                 cur_dir = self.change_dir(cur_dir)
#                 new_coord = [self.offset_list[cur_dir][0] + cur_coord[0], self.offset_list[cur_dir][1] + cur_coord[1]]
#
#             if (not self.check_position_validation(new_coord)):
#                 break
#             else:
#                 cur_coord = new_coord
#         return result
#
#     def change_dir(self, cur_dir):
#         if cur_dir < 3:
#             cur_dir += 1
#         else:
#             cur_dir = 0
#         return cur_dir
#
#     def check_position_validation(self, coord):
#         if coord[0] >= self.m or coord[1] >= self.n:
#             return False
#         elif self.is_visit_map[coord[0]][coord[1]] == 1:
#             return False
#         else:
#             return True
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        height, width = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        bound = {'up': 0, 'right': width - 1, "bottom": height - 1, "left": 0}
        x, y = 0, 0
        curDirect = 0
        while (self.isValidMove(x, y, bound)):
            ans.append(matrix[x][y])
            if self.isValidMove(x + directions[curDirect][0], y + directions[curDirect][1], bound):
                x = x + directions[curDirect][0]
                y = y + directions[curDirect][1]
            else:
                if curDirect == 0:
                    bound['up'] += 1
                elif curDirect == 1:
                    bound['right'] -= 1
                elif curDirect == 2:
                    bound['bottom'] -= 1
                else:
                    bound['left'] += 1
                curDirect = (curDirect + 1) % 4
                x = x + directions[curDirect][0]
                y = y + directions[curDirect][1]
        return ans

    def isValidMove(self, x, y, bound):
        if (bound['up'] <= x <= bound['bottom'] and bound['left'] <= y <= bound['right']):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.spiralOrder(matrix))
# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         # [row,col] -> [col,(n-1)-row]
#         # [2,2] -> [2,0]
#         n = len(matrix)
#         margin = 0
#         while(n-2*margin>1):
#             cur_x = margin
#             start = margin
#             end = n-margin-1
#             for i in range(start,end):
#                 cur_y = i
#                 cur_val =  matrix[cur_x][cur_y]
#                 for _ in range(4):
#                     next_x = cur_y
#                     next_y = (n-1) - cur_x
#                     next_val = matrix[next_x][next_y]
#                     matrix[next_x][next_y] = cur_val
#                     cur_val = next_val
#                     cur_x = next_x
#                     cur_y = next_y
#             margin+=1
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotateMatrix = [[0, -1],[1, 0]]
        n = len(matrix)
        rotateCenter = [n // 2, n // 2]
        rotatePositionSet = set([])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2 + n % 2):
                p = [i, j]
                value = matrix[j][i]
                real_p = p
                while (real_p[0] * n + real_p[1]) not in rotatePositionSet:
                    rotatePositionSet.add((real_p[0] * n + real_p[1]))
                    p = self.getNextPosition(rotateMatrix, rotateCenter, p)
                    real_p = self.convertPosition(p, n)
                    next_value = matrix[real_p[1]][real_p[0]]
                    matrix[real_p[1]][real_p[0]] = value
                    value = next_value

    def getNextPosition(self, rotateMatrix, rotateCenter, p):
        x, y = p[0], p[1]
        x_p = x - rotateCenter[0]
        y_p = y - rotateCenter[1]
        x = x_p * rotateMatrix[0][0] + y_p * rotateMatrix[0][1]
        y = x_p * rotateMatrix[1][0] + y_p * rotateMatrix[1][1]
        x = x + rotateCenter[0]
        y = y + rotateCenter[1]
        return [x, y]

    def convertPosition(self, p, n):
        if (n % 2 == 0):
            if p[0] > n // 2 and p[1] < n // 2:
                return [p[0] - 1, p[1]]
            if p[0] < n // 2 and p[1] > n // 2:
                return [p[0], p[1] - 1]
            if p[0] > n // 2 and p[1] > n // 2:
                return [p[0] - 1, p[1] - 1]

        return p

if __name__ == '__main__':
    solution = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    solution.rotate(matrix)
    print(matrix)

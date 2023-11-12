from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row
        up, bottom = 0, len(matrix) - 1
        while up < bottom:
            mid = (bottom + up + 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                up = mid
            else:
                bottom = mid - 1
        if matrix[up][0] == target: return True
        if matrix[up][0] > target: return False

        # search col
        left, right = 0, len(matrix[up]) - 1
        while left < right:
            mid = (right + left + 1) // 2
            if matrix[up][mid] == target:
                return True
            elif matrix[up][mid] < target:
                left = mid
            else:
                right = mid - 1
        return False
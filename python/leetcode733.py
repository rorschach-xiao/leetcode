from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = deque([(sr, sc)])
        origin_color = image[sr][sc]
        m, n = len(image), len(image[0])
        if origin_color == color:
            return image
        image[sr][sc] = color
        def isValidPos(r,c):
            return 0<=r<m and 0<=c<n
        while queue:
            cur_row, cur_col = queue.popleft()
            for offset in offsets:
                new_row = cur_row + offset[0]
                new_col = cur_col + offset[1]
                if isValidPos(new_row, new_col) and image[new_row][new_col] == origin_color:
                    image[new_row][new_col] = color
                    queue.append((new_row, new_col))
        return image
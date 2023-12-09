from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = deque([entrance])
        offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(maze), len(maze[0])

        def isValidPos(pos):
            return 0 <= pos[0] < m and 0 <= pos[1] < n

        def isBoarder(pos):
            return pos[0] == 0 or pos[1] == 0 or pos[0] == m - 1 or pos[1] == n - 1

        next_queue = deque()
        step = 0
        flag = False
        while queue:
            cur_pos = queue.popleft()
            if step > 0 and isBoarder(cur_pos):
                flag = True
                break
            maze[cur_pos[0]][cur_pos[1]] = '-'
            for offset in offsets:
                new_pos = [cur_pos[0] + offset[0], cur_pos[1] + offset[1]]
                if isValidPos(new_pos) and maze[new_pos[0]][new_pos[1]] == '.':
                    next_queue.append(new_pos)
                    maze[new_pos[0]][new_pos[1]] = "-"
            if len(queue) == 0:
                queue = next_queue
                next_queue = deque()
                step += 1

        return -1 if not flag else step
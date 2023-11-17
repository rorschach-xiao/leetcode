# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         self.h = len(grid)
#         self.w = len(grid[0])
#         self.offset = [[1,0],[0,1],[-1,0],[0,-1]]
#         self.grid = grid
#         num_of_island = 0
#         for i in range(self.h):
#             for j in range(self.w):
#                 if self.grid[i][j] == "1" :
#                     num_of_island += 1
#                     cur_island_queue = [[i,j]]
#                     while(len(cur_island_queue)!=0):
#                         cur_pos = cur_island_queue.pop()
#                         self.update_grid(cur_pos)
#                         for _offset in self.offset:
#                             new_pos = [cur_pos[0]+_offset[0],cur_pos[1]+_offset[1]]
#                             if self.check_position_validation(new_pos) and self.grid[new_pos[0]][new_pos[1]] == "1":
#                                 cur_island_queue.append(new_pos)
#                                 self.update_grid(cur_pos)
#         return num_of_island
#
#     def update_grid(self,coord):
#         self.grid[coord[0]][coord[1]] = "2"
#
#     def check_position_validation(self,coord):
#         if coord[0]>=self.h or coord[1]>=self.w or coord[0]<0 or coord[1]<0:
#             return False
#         else:
#             return True
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.numOfIsland = 0
        self._grid = grid
        m, n = len(self._grid), len(self._grid[0])
        self._offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if self._grid[i][j] == "1":
                    self.numOfIsland += 1
                    self._grid[i][j] = "2"
                    self.helper([i, j])
        return self.numOfIsland

    def helper(self, pos):
        def isValidPos(p):
            return 0 <= p[0] < len(self._grid) and 0 <= p[1] < len(self._grid[0])

        queue = [pos]
        while len(queue) > 0:
            cur = queue.pop(0)
            for offset in self._offsets:
                next_pos = [cur[0] + offset[0], cur[1] + offset[1]]
                if isValidPos(next_pos) and self._grid[next_pos[0]][next_pos[1]] == "1":
                    queue.append(next_pos)
                    self._grid[next_pos[0]][next_pos[1]] = "2"


if __name__=='__main__':
    solution = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(solution.numIslands(grid))

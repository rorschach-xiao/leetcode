class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.h = len(grid)
        self.w = len(grid[0])
        self.offset = [[1,0],[0,1],[-1,0],[0,-1]]
        self.grid = grid
        num_of_island = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == "1" :
                    num_of_island += 1
                    cur_island_queue = [[i,j]]
                    while(len(cur_island_queue)!=0):
                        cur_pos = cur_island_queue.pop()
                        self.update_grid(cur_pos)
                        for _offset in self.offset:
                            new_pos = [cur_pos[0]+_offset[0],cur_pos[1]+_offset[1]]
                            if self.check_position_validation(new_pos) and self.grid[new_pos[0]][new_pos[1]] == "1":
                                cur_island_queue.append(new_pos)
                                self.update_grid(cur_pos)
        return num_of_island

    def update_grid(self,coord):
        self.grid[coord[0]][coord[1]] = "2"

    def check_position_validation(self,coord):
        if coord[0]>=self.h or coord[1]>=self.w or coord[0]<0 or coord[1]<0:
            return False
        else:
            return True


if __name__=='__main__':
    solution = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(solution.numIslands(grid))

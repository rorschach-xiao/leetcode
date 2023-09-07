class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        self.h = h
        self.w = w
        offsets = [[0,1],[1,0],[0,-1],[-1,0]]
        max_area = 0
        is_visit = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1 and is_visit[i][j] == 0:
                    cur_island_pos_list = [[i,j]]
                    is_visit[i][j] = 1
                    cur_area = 0
                    while(len(cur_island_pos_list)!=0):
                        cur_pos = cur_island_pos_list.pop(0)
                        cur_area+=1
                        for _offset in offsets:
                            new_pos = [cur_pos[0]+_offset[0],cur_pos[1]+_offset[1]]
                            if self.is_valid_pos(new_pos) and grid[new_pos[0]][new_pos[1]] ==1 \
                            and is_visit[new_pos[0]][new_pos[1]] == 0:
                                cur_island_pos_list.append(new_pos)
                                is_visit[new_pos[0]][new_pos[1]] = 1
                    if cur_area >max_area:
                        max_area = cur_area
        return max_area


    def is_valid_pos(self,pos):
        if 0<=pos[0]<self.h and 0<=pos[1]<self.w:
            return True
        else:
            return False
if __name__ == '__main__':
    solution = Solution()
    grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0,0,0,0,0,0,0],
          [0,1,0,0,1,1,0,0,1,0,1,0,0],
          [0,1,0,0,1,1,0,0,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(solution.maxAreaOfIsland(grid))
# given a 2-D matrix , find the number of rectangle islands in it
# ex: input :
#      [[1, 1, 0, 0, 0],
#      [1, 1, 1, 0, 0],
#      [0, 0, 0, 1, 1],
#      [0, 1, 0, 1, 1]]
#     output : 2

class Solution():
    def numRectangleIslands(self, grid):
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        self.is_visit = [[0 for _ in range(w)] for _ in range(h)]
        self.offset = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        num_of_rect = 0
        find_island = False
        self.h = h
        self.w = w
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1 and self.is_visit[i][j] == 0:
                    idx_stack = []
                    idx_stack.append([i, j])
                    is_rect = True
                    find_island = True
                    while (len(idx_stack) != 0):
                        cur_idx = idx_stack.pop(-1)
                        self.is_visit[cur_idx[0]][cur_idx[1]]=1
                        right_idx = [cur_idx[0] + 1, cur_idx[1]]
                        down_idx = [cur_idx[0], cur_idx[1] + 1]
                        right_down_idx = [cur_idx[0] + 1, cur_idx[1] + 1]
                        if is_rect:
                            right_flag = self.is_good_point(right_idx, grid)
                            down_flag = self.is_good_point(down_idx, grid)
                            right_down_flag = self.is_good_point(right_down_idx, grid)
                            if (right_flag and down_flag and right_down_flag) or \
                                    (right_flag and not down_flag and not right_down_flag) or \
                                    (down_flag and not right_flag and not right_down_flag) or \
                                    (not right_flag and not down_flag and not right_down_flag):
                                is_rect = True
                            else:
                                is_rect = False

                        for _offset in self.offset:
                            new_idx = [cur_idx[0] + _offset[0], cur_idx[1] + _offset[1]]
                            if self.is_good_point(new_idx, grid):
                                idx_stack.append(new_idx)
                                self.is_visit[new_idx[0]][new_idx[1]] = 1
                                if _offset == [0, -1] or _offset == [-1, 0]:
                                    is_rect = False
                if find_island and is_rect:
                    num_of_rect += 1
                    find_island = False
        return num_of_rect

    def is_good_point(self, coord, grid):
        if self.is_position_valid(coord) and grid[coord[0]][coord[1]] == 1 \
            and self.is_visit[coord[0]][coord[1]] == 0:
            return True
        else:
            return False

    def is_position_valid(self, coord):
        if coord[0] < 0 or coord[0] >= self.h or coord[1] < 0 or coord[1] >= self.w:
            return False

        else:

            return True


solution = Solution()
grid = [[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 1]]
print(solution.numRectangleIslands(grid))
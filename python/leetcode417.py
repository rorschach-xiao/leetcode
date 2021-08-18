class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.heights = heights
        h = len(self.heights)
        w = len(self.heights[0])
        self.h = h
        self.w = w
        self.offset = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.po = [[0]*w for _ in range(h)]
        self.ao = [[0]*w for _ in range(h)]
        result_idx = []
        # pacific
        self.is_visit = [[0]*w for _ in range(h)]
        for i in range(h):
            self.dfs(i,0,True)
        self.is_visit = [[0]*w for _ in range(h)]
        for i in range(w):
            self.dfs(0,i,True)
        # atlantic
        self.is_visit = [[0]*w for _ in range(h)]
        for j in range(h):
            self.dfs(j,w-1,False)
        self.is_visit = [[0]*w for _ in range(h)]
        for j in range(w):
            self.dfs(h-1,j,False)
        # find common points

        for i in range(h):
            for j in range(w):
                if self.po[i][j] == 1 and self.ao[i][j] == 1:
                    result_idx.append([i,j])
        return result_idx


    def dfs(self, x, y, is_po):
        if self.is_visit[x][y] == 1:
            return
        self.is_visit[x][y] = 1
        if is_po:
            self.po[x][y] = 1
        else:
            self.ao[x][y] = 1
        for _offset in self.offset:
            new_x = x + _offset[0]
            new_y = y + _offset[1]

            if not self.is_pos_valid(new_x,new_y) or self.heights[new_x][new_y] < self.heights[x][y]:
                continue
            self.dfs(new_x,new_y,is_po)

    def is_pos_valid(self,x,y):
        if x<0 or x>=self.h or y<0 or y>=self.w:
            return False
        else:
            return True

if __name__ == '__main__':
    solution = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(solution.pacificAtlantic(heights))

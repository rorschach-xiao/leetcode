from heapq import heappop, heappush
class Solution:
    def maxPoints(self, grid, queries):
        self.m = len(grid)
        self.n = len(grid[0])
        self.offset = [[0,1],[1,0],[0,-1],[-1,0]]
        self.ans = 0
        self._stack = [(grid[0][0], 0, 0)]
        self.is_used = [[0 for _ in range(self.n)] for _ in range(self.m)]

        answers = [0 for _ in range(len(queries))]
        indexs = range(len(queries))
        queries_comb_indexs = zip(queries, indexs)
        queries_comb_indexs = sorted(queries_comb_indexs, key=lambda x:x[0])
        queries = [x[0] for x in queries_comb_indexs]
        indexs  = [x[1] for x in queries_comb_indexs]
        last_query = -1
        last_ans = -1

        for i, query in enumerate(queries):
            if last_query == query:
                ans = last_ans
            else:
                ans = self.maxPoints_simple(grid, query)
            answers[indexs[i]] = ans
            last_query = query
            last_ans = ans
        return answers

    def maxPoints_simple(self, grid, query):
        m = self.m
        n = self.n
        if grid[0][0] >= query:
            return 0
        while(len(self._stack) != 0 and self._stack[0][0] < query):
            _, i, j = heappop(self._stack)

            if grid[i][j] < query and self.is_used[i][j] != 1:
                self.ans += 1
                self.is_used[i][j] = 1
                for offset in self.offsets:
                    y_o, x_o = offset
                    if self.is_valid(j + x_o, i + y_o, m, n) and self.is_used[i + y_o][j + x_o] == 0:
                        heappush(self._stack, (grid[i + y_o][j + x_o], i + y_o, j + x_o))
                        self.is_used[i + y_o][j + x_o] = 2

        return self.ans


    def is_valid(self, x, y, h, w):
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5, 5, 6, 2]
    print(solution.maxPoints(grid,queries))

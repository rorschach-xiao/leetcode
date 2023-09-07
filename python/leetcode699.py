class Solution:
    def fallingSquares(self, positions):
        intervals = [[1, float('inf')]]
        intervals_height = [0]
        ans = []
        for pos in positions:
            for i, interval in enumerate(intervals):
                # update interval
                if pos[0] >= interval[0] and pos[0] < interval[1]:
                    start_i = i
                if pos[0] + pos[1] >= interval[0] and pos[0] + pos[1] < interval[1]:
                    end_i = i
                    break

            if pos[0] >= interval[0] and pos[0] + pos[1] < interval[1]:
                left = [interval[0], pos[0]]
                middle = [pos[0], pos[0]+pos[1]]
                right = [pos[0]+pos[1], interval[1]]
                new_intervals = [left, middle, right]
                cnt = 0
                intervals.pop(i)
                cur_h = intervals_height.pop(i)
                for j, new_inter in enumerate(new_intervals):
                    if j == 1:
                        new_h = cur_h + pos[1]
                    else:
                        new_h = cur_h
                    if new_inter[1] - new_inter[0] > 0:
                        intervals.insert(i + cnt, new_inter)
                        intervals_height.insert(i + cnt, new_h)
                        cnt += 1

                # update interval height




if __name__ == '__main__':
    solution = Solution()

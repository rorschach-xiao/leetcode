class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_interval = sorted(intervals)
        new_interval = []
        num_of_inter = len(sorted_interval)
        if num_of_inter==1:
            return intervals
        i=1
        cur_inter = sorted_interval[0]
        while i < num_of_inter:
            next_inter = sorted_interval[i]
            if cur_inter[1]>=next_inter[1]:
                i+=1
                continue
            elif cur_inter[1]>=next_inter[0]:
                cur_inter[1] = next_inter[1]
            else:
                new_interval.append(cur_inter)
                cur_inter = next_inter
            i+=1
        new_interval.append(cur_inter)
        return new_interval
if __name__ =='__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    solution = Solution()
    print(solution.merge(intervals))
class Solution(object):
    # def insert(self, intervals, newInterval):
    #     """
    #     :type intervals: List[List[int]]
    #     :type newInterval: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     pre_end = -1
    #     insert_pos = None
    #     i = 0
    #     while i < len(intervals):
    #         interval = intervals[i]
    #         if insert_pos is None:
    #             if interval[0] >= newInterval[0] > pre_end or interval[1] >= newInterval[0] >= interval[0]:
    #                 # find insertion position
    #                 insert_pos = i
    #                 if interval[0] > newInterval[1]:
    #                     intervals.insert(insert_pos, newInterval)
    #                     break
    #                 elif interval[1] >= newInterval[1]:
    #                     intervals[i] = [min(interval[0], newInterval[0]), interval[1]]
    #                     break
    #                 else:
    #                     intervals[i] = [min(interval[0], newInterval[0]), newInterval[1]]
    #                 i += 1
    #                 continue
    #             pre_end = interval[1]
    #             i += 1
    #         else:
    #             if intervals[insert_pos][1] >= interval[0]:
    #                 intervals.pop(i)
    #                 intervals[insert_pos][1] = max(interval[1], intervals[insert_pos][1])
    #             else:
    #                 break
    #     if insert_pos is None:
    #         intervals.append(newInterval)
    #
    #     return intervals
    #
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insert = False
        ans = []
        for li, ri in intervals:
            if li > newInterval[1]: # new interval is on the left
                if not insert:
                    ans.append(newInterval)
                    insert = True
                ans.append([li, ri])
            elif ri < newInterval[0]: # new interval is on the right
                ans.append([li, ri])
            else:
                newInterval[0] = min(li, newInterval[0])
                newInterval[1] = max(ri, newInterval[1])

        if not insert:
            ans.append(newInterval)

        return ans





if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1,3],[6,9]], [2,5]))
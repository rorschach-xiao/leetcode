from typing import List


class Solution:

    # dynamic programming
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        dp = [1 for _ in range(n)]
        res = 1
        for i in range(1, n):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])

        return n - res

    # greedy
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        res = 1
        for i in range(1, n):
            if intervals[i][0] >= right:
                res += 1
                right = intervals[i][1]

        return n - res


from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lineSet = defaultdict()
        n = len(points)
        maxNumOfPoints = float("-inf")
        for i in range(n):
            for j in range(i + 1, n):
                slope, intercept = self.calculateLine(points[i], points[j])
                if (slope, intercept) not in lineSet:
                    lineSet[(slope, intercept)] = {str(points[i]), str(points[j])}
                else:
                    lineSet[(slope, intercept)].add(str(points[i]))
                    lineSet[(slope, intercept)].add(str(points[j]))
                maxNumOfPoints = max(maxNumOfPoints, len(lineSet[(slope, intercept)]))
        return maxNumOfPoints

    def calculateLine(self, p1, p2):
        if p1[0] == p2[0]:
            return (float("inf"), p1[0])
        slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
        intercept = p1[1] - slope * p1[0]
        return (slope, intercept)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]]))
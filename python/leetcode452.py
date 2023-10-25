from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points = sorted(points)
        count = 1
        current_intersection = points[0]
        for i, point in enumerate(points):
            if point[0] <= current_intersection[1]:
                current_intersection[0] = max(current_intersection[0], point[0])
                current_intersection[1] = min(current_intersection[1], point[1])
            else:
                count += 1
                current_intersection = point
        return count
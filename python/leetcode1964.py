from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        if n == 1:
            return [1]
        tails = [obstacles[0]]
        ans = [1]
        cnt = 1
        for i in range(1, n):
            if tails[-1] <= obstacles[i]:
                tails.append(obstacles[i])
                cnt += 1
                ans.append(cnt)
            else:
                left, right = 0, len(tails) - 1
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] > obstacles[i]:
                        right = mid
                    else:
                        left = mid + 1
                tails[left] = obstacles[i]
                ans.append(left + 1)
        return ans

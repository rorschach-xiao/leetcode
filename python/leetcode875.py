from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTotalTime(k):
            nonlocal piles
            total_time = 0
            for pile in piles:
                total_time += (pile + k - 1) // k
            return total_time

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if calcTotalTime(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    solution = Solution()
    solution.minEatingSpeed([3,6,7,11], 8)
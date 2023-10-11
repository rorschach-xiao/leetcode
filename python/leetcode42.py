from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        start, end, n = 0, 0, len(height)
        total_trap_volume = 0
        if n < 3:
            return 0
        for i in range(1, n):
            if height[i] >= height[start]:
                total_trap_volume += self.computeTrapUnit(height, start, i)
                start = i
        end = n-1
        for j in range(n-2, -1, -1):
            if height[j] > height[end]:
                total_trap_volume += self.computeTrapUnit(height, j, end)
                end = j
        return total_trap_volume

    def computeTrapUnit(self, height, start, end):
        level = min(height[start], height[end])
        volume = 0
        for i in range(start + 1, end):
            volume += max(level - height[i], 0)
        return volume 

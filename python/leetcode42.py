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

# Two Pointers

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        cur_unit_sum = 0
        for right in range(1, n):
            if height[left] > height[right]:
                cur_unit_sum += height[left] - height[right]
            else:
                left = right
                ans += cur_unit_sum
                cur_unit_sum = 0
        right = n-1
        cur_unit_sum = 0
        for left in range(n - 2, -1, -1):
            if height[left] < height[right]:
                cur_unit_sum += height[right] - height[left]
            else:
                right = left
                ans += cur_unit_sum
                cur_unit_sum = 0

        return ans



from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxdp = [0 for _ in range(n)]
        mindp = [0 for _ in range(n)]
        maxdp[0] = nums[0]
        mindp[0] = nums[0]
        ans = maxdp[0]
        for i in range(1, n):
            maxdp[i] = max(nums[i], nums[i] * maxdp[i-1], nums[i] * mindp[i-1])
            mindp[i] = min(nums[i], nums[i] * maxdp[i-1], nums[i] * mindp[i-1])
            ans = max(ans, maxdp[i])
        return ans
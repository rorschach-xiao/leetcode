from typing import List

# O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = nums[0]
        maxSum = preSum
        for i in range(1, n):
            curMaxSum = max(nums[i], preSum + nums[i])
            preSum = curMaxSum
            maxSum = max(maxSum, curMaxSum)
        return maxSum


from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # find maxSum and minSum of the subarray
        preMaxSum = nums[0]
        preMinSum = nums[0]
        maxSum = preMaxSum
        minSum = preMinSum
        totalSum = nums[0]
        for i in range(1, n):
            curMaxSum = max(nums[i], nums[i] + preMaxSum)
            curMinSum = min(nums[i], nums[i] + preMinSum)
            preMinSum = curMinSum
            preMaxSum = curMaxSum
            minSum = min(minSum, curMinSum)
            maxSum = max(maxSum, curMaxSum)
            totalSum += nums[i]

        if totalSum != minSum:
            return max(maxSum, totalSum - minSum)
        else:
            return maxSum
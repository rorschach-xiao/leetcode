from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        preSum = [0 for _ in range(n)]
        postSum = [0 for _ in range(n)]
        preSum[0] = nums[0]
        postSum[-1] = nums[-1]
        for i in range(1, n):
            preSum[i] = preSum[i-1] + nums[i]
            postSum[n-i-1] = postSum[n-i] + nums[n-i-1]
        for i in range(n):
            if preSum[i] == postSum[i]:
                return i
        return -1
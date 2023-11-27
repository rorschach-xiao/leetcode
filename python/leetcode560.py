from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum = 0
        preSum = {}
        preSum[0] = 1
        res = 0
        for i in range(n):
            cur_sum += nums[i]
            if cur_sum - k in preSum:
                res += preSum[cur_sum - k]
            if cur_sum not in preSum:
                preSum[cur_sum] = 1
            else:
                preSum[cur_sum] += 1
        return res
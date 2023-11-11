from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        n = len(nums)
        if n == k:
            return round(sum(nums) / k,5)
        head = 0
        cur_sum = 0
        for i in range(n):
            if i < k - 1:
                cur_sum += nums[i]
            else:
                cur_sum += nums[i]
                if i >= k:
                    cur_sum -= nums[head]
                    head += 1
                max_sum = max(max_sum, cur_sum)
        return round(max_sum / k, 5)
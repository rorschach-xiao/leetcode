from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        preSumReminder = {0: -1}
        reminder = 0
        for i in range(n):
            reminder = (reminder + nums[i]) % k
            if reminder in preSumReminder:
                preIndex = preSumReminder[reminder]
                if i - preIndex >= 2:
                    return True
            else:
                preSumReminder[reminder] = i

        return False
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSumReminder = {0: 1}
        reminder = 0
        res = 0
        for i in range(n):
            reminder = (reminder + nums[i]) % k
            if reminder in preSumReminder:
                res +=  preSumReminder[reminder]
                preSumReminder[reminder] += 1
            else:
                preSumReminder[reminder] = 1
        return res
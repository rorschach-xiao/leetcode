from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        maxRob = float('-inf')
        # rob 0 ~ n - 2
        prePre = 0
        pre = nums[0]
        # rob 1 ~ n - 1
        prePre2 = 0
        pre2 = nums[1]
        for i in range(1, n - 1):
            cur1 = max(pre, prePre + nums[i])
            cur2 = max(pre2, prePre2 + nums[i + 1])
            maxRob = max(maxRob, cur1, cur2)
            prePre = pre
            pre = cur1
            prePre2 = pre2
            pre2 = cur2
        maxRob = max(maxRob, pre, pre2)

        return maxRob
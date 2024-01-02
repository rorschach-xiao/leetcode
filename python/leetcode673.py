from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        tails = {1: [nums[0]]}
        cnt = {1: [1]}
        L = 1
        for i in range(1, n):
            if nums[i] > tails[L][-1]:
                L += 1
                tails[L] = [nums[i]]
                p = self.bisect(0, len(tails[L - 1]) - 1, lambda k: tails[L - 1][k] < nums[i])
                cnt[L] = [sum(cnt[L - 1][p:])]

            else:
                curLen = self.bisect(1, L, lambda l: tails[l][-1] >= nums[i])
                tails[curLen].append(nums[i])
                if curLen == 1:
                    cnt[1].append(1)
                else:
                    p = self.bisect(0, len(tails[curLen - 1]) - 1, lambda k: tails[curLen - 1][k] < nums[i])
                    cnt[curLen].append(sum(cnt[curLen - 1][p:]))

        return sum(cnt[L])

    def bisect(self, low, high, func):
        left, right = low, high
        while left < right:
            mid = (left + right) // 2
            if func(mid):
                right = mid
            else:
                left = mid + 1
        return left

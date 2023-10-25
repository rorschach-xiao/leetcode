from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]
        start, end = 0, 0
        ans = []

        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                end += 1
            else:
                if start == end:
                    ans.append(f"{nums[start]}")
                else:
                    ans.append(f"{nums[start]}->{nums[end]}")
                start = i
                end = i

        if start == end:
            ans.append(f"{nums[start]}")
        else:
            ans.append(f"{nums[start]}->{nums[end]}")
        return ans
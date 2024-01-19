import copy
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.ans = []
        self.visit = set()
        self.helper([], self.visit)
        return self.ans

    def helper(self, cur_perm, visited_idx):
        if len(cur_perm) == len(self.nums):
            self.ans.append(copy.copy(cur_perm))
            return

        for i, num in enumerate(self.nums):
            if i in visited_idx or (i > 0 and num == self.nums[i-1] and i - 1 not in visited_idx):
                continue
            else:
                cur_perm.append(num)
                visited_idx.add(i)
                self.helper(cur_perm, visited_idx)
                cur_perm.pop(-1)
                visited_idx.remove(i)
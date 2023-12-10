import copy
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.k = k
        self.n = n
        self.dfs([], 1, 0)
        return self.ans

    def dfs(self, cur_comb, num, cur_sum):
        if cur_sum > self.n:
            return
        if len(cur_comb) == self.k:
            if cur_sum == self.n:
                self.ans.append(copy.deepcopy(cur_comb))
            return

        for i in range(num, 10):
            cur_comb.append(i)
            self.dfs(cur_comb, i + 1, cur_sum + i)
            cur_comb.pop()
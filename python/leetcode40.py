# class Solution:
#     def combinationSum2(self, candidates, target):
#         candidates = sorted(candidates)
#         self.results = []
#         cur_comb = []
#         self.helper(candidates, target, cur_comb)
#         return self.results
#
#     def helper(self, candidates, target, cur_comb):
#         if target == 0:
#             self.results.append(list(cur_comb))
#             return
#         pre_element = None
#         for i, candidate in enumerate(candidates):
#             cur_element = candidates[i]
#             if pre_element is not None and pre_element == cur_element:
#                 continue
#             cur_comb.append(cur_element)
#             if target - cur_element >= 0:
#                 self.helper(candidates[i+1:], target - cur_element, cur_comb)
#             else:
#                 cur_comb.pop(-1)
#                 break
#             cur_comb.pop(-1)
#             pre_element = cur_element
import copy
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        n = len(candidates)
        def dfs(comb, i, curSum):
            if curSum == target:
                ans.append(copy.copy(comb))
                return
            elif curSum > target:
                return
            else:
                for j in range(i, n):
                    if j > i and candidates[j] == candidates[j-1]:
                        continue
                    comb.append(candidates[j])
                    dfs(comb, j+1, curSum + candidates[j])
                    comb.pop()
        dfs([], 0, 0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    print(solution.combinationSum2(candidates, target))
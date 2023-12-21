from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1 for _ in range(n)]
        for i in range(n * 2 - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                index = stack.pop()
                ans[index] = nums[i % n]
            stack.append(i % n)
        return ans
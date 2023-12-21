from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        ans = [-1 for _ in range(n1)]
        valueDict = {}
        for i, n in enumerate(nums1):
            valueDict[n] = i

        stack = []
        for j in range(n2):
            while stack and stack[-1] < nums2[j]:
                val = stack.pop()
                if val in valueDict:
                    ans[valueDict[val]] = nums2[j]
            stack.append(nums2[j])
        return ans
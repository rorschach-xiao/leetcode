from typing import List, Optional

from utils.Tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        mid = n // 2
        root = TreeNode(nums[mid])
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        root.left = left
        root.right = right
        return root
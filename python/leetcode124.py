from typing import Optional

from utils.Tree import TreeNode


class Solution:
    maxSum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.maxSum

    def helper(self, root) -> int:
        if root is None:
            return 0
        leftMaxPathSum = max(self.helper(root.left), 0)
        rightMaxPathSum = max(self.helper(root.right), 0)
        self.maxSum = max(self.maxSum, root.val + leftMaxPathSum + rightMaxPathSum)
        return root.val + max(leftMaxPathSum, rightMaxPathSum)
from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val

        hasPathLeft = self.hasPathSum(root.left, targetSum - root.val)
        hasPathRight = self.hasPathSum(root.right, targetSum - root.val)
        return hasPathLeft or hasPathRight
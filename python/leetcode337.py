from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            la, lb = dfs(node.left)
            ra, rb = dfs(node.right)
            return node.val + lb + rb, max(la, lb) + max(ra, rb)

        return max(dfs(root))
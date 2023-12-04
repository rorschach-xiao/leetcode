from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        self.dfs(leaves1, root1)
        self.dfs(leaves2, root2)
        return leaves1 == leaves2

    def dfs(self, leaves, node):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
            return
        if node.left:
            self.dfs(leaves, node.left)
        if node.right:
            self.dfs(leaves, node.right)
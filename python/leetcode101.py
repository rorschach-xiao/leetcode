from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        revertedTree = self.revertTree(root)
        return self.isSameTree(root, revertedTree)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (q is None and p is not None):
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def revertTree(self, root):
        if root is None:
            return root
        root_copy = TreeNode(root.val)
        left = self.revertTree(root.left)
        right = self.revertTree(root.right)
        root_copy.left = right
        root_copy.right = left
        return root_copy
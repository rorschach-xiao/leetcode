from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        elif root.val > val:
            return self.searchBST(root.left, val)

        else:
            return self.searchBST(root.right, val)
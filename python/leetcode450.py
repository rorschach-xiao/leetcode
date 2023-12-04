from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else :
            root.right = self.deleteNode(root.right, key)
        return root
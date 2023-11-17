from typing import Optional

from utils.Tree import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = -1
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root is None or self.k == 0:
            return
        self.dfs(root.left)
        if self.k > 0:
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                return
        self.dfs(root.right)
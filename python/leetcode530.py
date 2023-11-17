from typing import Optional

from utils.Tree import TreeNode


class Solution:
    MAX_INT = 10 ** 5 + 1

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.pre = -1
        self.ans = self.MAX_INT
        self.dfs(root)
        return self.ans

    def dfs(self, cur):
        if cur is None:
            return
        self.dfs(cur.left)
        if self.pre == -1:
            self.pre = cur.val
        else:
            self.ans = min(self.ans, abs(cur.val) - self.pre)
            self.pre = cur.val
        self.dfs(cur.right)
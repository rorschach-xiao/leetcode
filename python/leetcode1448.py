from utils.Tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        self.dfs(float("-inf"), root)
        return self.cnt

    def dfs(self, maxValue, node):
        if not node:
            return
        if node.val >= maxValue:
            maxValue = node.val
            self.cnt += 1
        self.dfs(maxValue, node.left)
        self.dfs(maxValue, node.right)
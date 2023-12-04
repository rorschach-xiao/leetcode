from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0, 'left')
        self.dfs(root, 0, 'right')
        return self.res



    def dfs(self, node, curLen, direction):
        if not node:
            return
        if curLen > self.res:
            self.res = curLen
        if direction == 'left':
            self.dfs(node.left, curLen + 1, 'right')
            self.dfs(node.right, 1, 'left')

        elif direction == 'right':
            self.dfs(node.right, curLen + 1, 'left')
            self.dfs(node.left, 1, 'right')

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode.list_2_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
    print(solution.longestZigZag(root))
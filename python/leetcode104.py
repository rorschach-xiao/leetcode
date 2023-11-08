from typing import Optional
from utils.Tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

if __name__ == '__main__':
    solution = Solution()
    l = [3,9,20,None,None,15,7]
    root = TreeNode.list_2_tree(l)
    print(solution.maxDepth(root))

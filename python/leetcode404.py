# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_sum = 0

        def dfs(root):
            nonlocal left_sum
            if root is None:
                return
            if root.left is not None:
                if self.isLeaves(root.left):
                    left_sum += root.left.val
                else:
                    dfs(root.left)
            if root.right is not None:
                dfs(root.right)
        dfs(root)
        return left_sum
    def isLeaves(self,root):
        return  root.left is None and root.right is None

if __name__ == '__main__':
    from leetcode297 import Codec

    codec = Codec()
    tree = '[3,9,20,null,null,15,7]'
    root = codec.deserialize(tree)
    solution = Solution()
    print(solution.sumOfLeftLeaves(root))
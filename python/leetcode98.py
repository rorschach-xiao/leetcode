class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    pre = float('-inf')
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if (not self.isValidBST(root.left)):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        if (not self.isValidBST(root.right)):
            return False
        return True
    
if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(solution.isValidBST(root))
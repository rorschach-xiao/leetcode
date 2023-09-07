class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.targetSum = targetSum
        self.result = []
        path = []
        self.dfs(root, path)
        return self.result

    def dfs(self, root, path):
        path.append(root.val)
        if root.left is None and root.right is None:
            if sum(path) == self.targetSum:
                self.result.append(path.copy())
            path.pop(-1)
            return
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)
        path.pop(-1)
if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.pathSum(root,4))
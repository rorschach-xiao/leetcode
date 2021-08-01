class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = []
        path = []
        self.dfs(root,path)
        return sum(self.result)

    def dfs(self,root,path):
        path.append(root.val)
        if root.left is None and root.right is None:
            cur_path_val = 0
            for val in path:
                cur_path_val = cur_path_val*10 + val
            self.result.append(cur_path_val)
        if root.left:
            self.dfs(root.left,path)
        if root.right:
            self.dfs(root.right,path)
        path.pop(-1)
if __name__ =='__main__':
    solution=Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    print(solution.sumNumbers(root))
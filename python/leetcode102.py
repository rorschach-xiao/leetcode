# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        cur_node = root
        cur_level_list = [cur_node]
        while(len(cur_level_list)!=0):
            next_level_list = []
            cur_val_list = []
            for node in cur_level_list:
                cur_val_list.append(node.val)
                if node.left is not None:
                    next_level_list.append(node.left)
                if node.right is not None:
                    next_level_list.append(node.right)
            cur_level_list = next_level_list
            result.append(cur_val_list)
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    solution = Solution()
    print(solution.levelOrder(root))
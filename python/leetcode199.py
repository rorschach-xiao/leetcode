# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return []
        cur_node = root
        cur_level_list = [cur_node]
        while(len(cur_level_list)!=0):
            next_level_list = []
            result.append(cur_level_list[-1].val)
            for node in cur_level_list:
                if node.left is not None:
                    next_level_list.append(node.left)
                if node.right is not None:
                    next_level_list.append(node.right)
            cur_level_list = next_level_list
        return result
    
if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.rightSideView(root))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _stack = []
        _stack.append(root)
        empty_flag = 0
        while(len(_stack) !=0):
            cur_node = _stack.pop(0)
            if cur_node is None :
                if empty_flag == 0:
                    empty_flag = 1
                continue
            elif cur_node is not None and empty_flag == 1:
                return False
            else:
                _stack.append(cur_node.left)
                _stack.append(cur_node.right)

        return True

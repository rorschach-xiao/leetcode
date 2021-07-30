# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        self.cur_order = 0 # 0--left2right 1--right2left
        self.result = []
        cur_level_list = [root]
        while(len(cur_level_list)!=0):
            next_level_list = []
            cur_val_list = []
            for i in range(len(cur_level_list)):
                cur_val_list.append(cur_level_list[i].val)
                if cur_level_list[i].left is not None:
                    next_level_list.append(cur_level_list[i].left)
                if cur_level_list[i].right is not None:
                    next_level_list.append(cur_level_list[i].right)
            cur_level_list = next_level_list
            if self.cur_order == 0:
                self.result.append(cur_val_list)
                self.cur_order = 1
            elif self.cur_order == 1:
                cur_val_list.reverse()
                self.result.append(cur_val_list)
                self.cur_order = 0
        return self.result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    solution = Solution()
    solution.zigzagLevelOrder(root)

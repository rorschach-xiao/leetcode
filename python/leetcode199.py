# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         if root is None:
#             return []
#         cur_node = root
#         cur_level_list = [cur_node]
#         while(len(cur_level_list)!=0):
#             next_level_list = []
#             result.append(cur_level_list[-1].val)
#             for node in cur_level_list:
#                 if node.left is not None:
#                     next_level_list.append(node.left)
#                 if node.right is not None:
#                     next_level_list.append(node.right)
#             cur_level_list = next_level_list
#         return result
from typing import Optional, List

from utils.Tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if not root:
            return view
        cur_level = [root]
        next_level = []
        while cur_level:
            cur = cur_level.pop(0)
            if cur.left:
                next_level.append(cur.left)
            if cur.right:
                next_level.append(cur.right)
            if len(cur_level) == 0:
                view.append(cur.val)
                cur_level = next_level
                next_level = []

        return view

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.rightSideView(root))

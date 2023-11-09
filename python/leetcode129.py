# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def sumNumbers(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.result = []
#         path = []
#         self.dfs(root,path)
#         return sum(self.result)
#
#     def dfs(self,root,path):
#         path.append(root.val)
#         if root.left is None and root.right is None:
#             cur_path_val = 0
#             for val in path:
#                 cur_path_val = cur_path_val*10 + val
#             self.result.append(cur_path_val)
#         if root.left:
#             self.dfs(root.left,path)
#         if root.right:
#             self.dfs(root.right,path)
#         path.pop(-1)
from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0, 0)

    def helper(self, root:Optional[TreeNode] , current_sum: int, current_value: int) -> int:
        if root is None:
            return 0
        current_value = current_value * 10 + root.val
        if root.left is None and root.right is None:
            current_sum += current_value
            return current_sum
        left_sum = self.helper(root.left, current_sum, current_value)
        right_sum = self.helper(root.right, current_sum, current_value)
        return left_sum + right_sum

if __name__ =='__main__':
    solution=Solution()
    root = TreeNode.list_2_tree([4,9,0,5,1])
    print(solution.sumNumbers(root))
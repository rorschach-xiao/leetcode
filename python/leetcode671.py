# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return -1
        else:
            if root.left.val != root.right.val:
                if root.left.val < root.right.val:
                    left_second_min = self.findSecondMinimumValue(root.left)
                    right_second_min = root.right.val
                else:
                    left_second_min = root.left.val
                    right_second_min = self.findSecondMinimumValue(root.right)

            else:
                left_second_min = self.findSecondMinimumValue(root.left)
                right_second_min = self.findSecondMinimumValue(root.right)

            if left_second_min == -1 or right_second_min == -1:
                return max(left_second_min, right_second_min)
            else:
                return min(left_second_min, right_second_min)
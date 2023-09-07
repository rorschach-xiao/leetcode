# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        self.in_dict = {}
        for idx, val in enumerate(inorder):
            self.in_dict[val] = idx
        root = self.helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        return root

    def helper(self, pre_l, pre_r, in_l, in_r):
        if pre_r < pre_l or in_r < in_l:
            return None
        root_val = self.preorder[pre_l]
        root = TreeNode(self.preorder[pre_l])
        left_in_l = in_l
        left_in_r = self.in_dict[root_val] - 1
        right_in_l = left_in_r + 2
        right_in_r = in_r
        left_pre_l = pre_l + 1
        left_pre_r = left_pre_l + (left_in_r - left_in_l) + 1
        right_pre_l = left_pre_r
        right_pre_r = right_pre_l + (right_in_r - right_in_l) + 1
        root.left = self.helper(left_pre_l, left_pre_r, left_in_l, left_in_r)
        root.right = self.helper(right_pre_l, right_pre_r, right_in_l, right_in_r)
        return root

if __name__ == '__main__':
    solution = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = solution.buildTree(preorder,inorder)
from typing import List, Optional

from utils.Tree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self._inorder = inorder
        self._postorder = postorder
        self._dict = {}
        if len(inorder) == 0:
            return None
        for i, n in enumerate(inorder):
            self._dict[n] = i

        return self.helper(0, len(inorder) - 1, 0, len(postorder) - 1)



    def helper(self, inorder_l, inorder_r, postorder_l, postorder_r):
        root_val = self._postorder[postorder_r]
        root = TreeNode(root_val)
        if inorder_l == inorder_r:
            return root
        elif inorder_l > inorder_r:
            return None
        root_idx = self._dict[root_val]
        left_len = root_idx - inorder_l - 1
        left_tree = self.helper(inorder_l, root_idx - 1, postorder_l, postorder_l + left_len)
        right_tree = self.helper(root_idx + 1, inorder_r, postorder_l + left_len + 1, postorder_r - 1)
        root.left = left_tree
        root.right = right_tree
        return root

if __name__ == '__main__':
    solution = Solution()
    inorder = [2, 1]
    postorder = [2, 1]
    root = solution.buildTree(inorder, postorder)
    print(TreeNode.tree_2_list(root))
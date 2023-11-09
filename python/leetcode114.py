from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head, _ = self.helper(root)
        return head

    def helper(self, root) -> [TreeNode, TreeNode]:
        " return the head and tail of the linked list"
        if root is None:
            return [None, None]

        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)
        root.left = None
        if left_head is not None:
            root.right = left_head
            left_tail.right = right_head
            left_tail.left = None
        else:
            root.right = right_head

        if right_tail is not None:
            return [root, right_tail]
        elif left_tail is not None:
            return [root, left_tail]
        return [root, root]

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode.list_2_tree([1,2,None,3])
    solution.flatten(root)
    print(TreeNode.tree_2_list(root))

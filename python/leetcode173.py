# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from utils.Tree import TreeNode


# class BSTIterator:
#     def __init__(self, root: TreeNode):
#         self.stack = [root]
#         while(True):
#             if self.stack[-1].left is None:
#                 break
#             else:
#                 self.stack.append(self.stack[-1].left)
#
#     def next(self) -> int:
#         while (self.stack[-1].left is not None):
#             self.stack.append(self.stack[-1].left)
#         leave = self.stack.pop(-1)
#         if len(self.stack) != 0:
#             self.stack[-1].left = None
#         if leave.right is not None:
#             self.stack.append(leave.right)
#         return leave.val
#
#     def hasNext(self) -> bool:
#         if len(self.stack) > 0:
#             return True
#         else:
#             return False

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iter = []
        self._push(root)

    def _push(self, node):
        cur = node
        while cur:
            self.iter.append(cur)
            cur = cur.left

    def next(self) -> int:
        node = self.iter.pop()
        self._push(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.iter) != 0

if __name__ == '__main__':
    from leetcode297 import Codec

    codec = Codec()
    tree = '[7, 3, 15, null, null, 9, 20]'
    root = codec.deserialize(tree)
    obj = BSTIterator(root)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
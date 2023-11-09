class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        pre = None
        level = [root]
        next_level = []
        while(len(level) != 0):
            cur = level.pop(0)
            if cur is not None:
                next_level.append(cur.left)
                next_level.append(cur.right)
                if pre is not None:
                    pre.next = cur
                pre = cur
            if len(level) == 0:
                level = next_level
                next_level = []
                pre = None

        return root
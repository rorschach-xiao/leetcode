class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def list_2_tree(cls, l):
        if len(l) == 0:
            return None
        stack = []
        root = cls(l.pop(0))
        stack.append(root)
        while len(l) > 0 :
            cur = stack.pop(0)
            l_v = l.pop(0)
            r_v = l.pop(0)
            if l_v is not None:
                left_node = cls(l_v)
                cur.left = left_node
                stack.append(left_node)
            if r_v is not None:
                right_node = cls(r_v)
                cur.right = right_node
                stack.append(right_node)

        return root

    @classmethod
    def tree_2_list(cls, root):
        if root is None:
            return []
        l = []
        cur_level = [root]
        while (len(cur_level) != 0):
            cur = cur_level.pop(0)
            if cur is not None:
                l.append(cur.val)
                cur_level.append(cur.left)
                cur_level.append(cur.right)
            else:
                l.append(None)
        return l

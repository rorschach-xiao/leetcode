# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        cur_layer_nodes = [root]
        while(True):
            next_layer_nodes = []
            idx_x,idx_y = None,None
            flag = True
            for i,node in enumerate(cur_layer_nodes):
                if node is None:
                    continue
                else:
                    if node.val == x:
                        idx_x = i
                    if node.val == y:
                        idx_y = i
                    if node.left is not None or node.right is not None:
                        flag = False
                    next_layer_nodes.append(node.left)
                    next_layer_nodes.append(node.right)
            cur_layer_nodes = next_layer_nodes

            if idx_x is None or idx_y is None:
                if (idx_x is None and idx_y is not None) or (idx_x is not None and idx_y is None):
                    return False
                else:
                    if flag:
                        break
                    else:
                        continue
            else:
                if (idx_x // 2) == (idx_y // 2) :
                    return False
                else:
                    return True
        return False



if __name__ == '__main__':
    from leetcode297 import Codec
    codec = Codec()
    tree = '[1,2,3,null,4,null,5]'
    root = codec.deserialize(tree)
    solution = Solution()
    print(solution.isCousins(root,5,4))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        cur = root
        cur_layer_nodes = [cur]
        result = []
        while(True):
            next_layer_nodes = []
            cur_layer_max = float('-inf')
            for node in cur_layer_nodes:
                if node.val > cur_layer_max:
                    cur_layer_max = node.val
                if node.left is not None:
                    next_layer_nodes.append(node.left)
                if node.right is not None:
                    next_layer_nodes.append(node.right)
            result.append(cur_layer_max)
            cur_layer_nodes = next_layer_nodes
            if len(next_layer_nodes) == 0:
                break
        return result

if __name__ == '__main__':
    from leetcode297 import Codec
    codec = Codec()
    tree = '[1,3,2,5,3,null,9]'
    root = codec.deserialize(tree)
    solution = Solution()
    solution.largestValues(root)





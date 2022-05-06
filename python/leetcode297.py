# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root: return ''
    #     queue = [root]
    #     layer = []
    #     out = [str(root.val)]
    #     layer_flg = 0
    #     while True:
    #         print(layer, queue, len(queue))
    #         if len(queue) == 0 and not layer_flg:
    #             break
    #         cur_node = queue.pop(0)
    #         if cur_node is None:
    #             continue
    #         l = 'null' if not cur_node.left else str(cur_node.left.val)
    #         r = 'null' if not cur_node.right else str(cur_node.right.val)
    #         print('----', l, r, layer, queue)
    #         if l == 'null' and r == 'null' and len(queue)==0 and (len(layer)==0 or not layer_flg):
    #             break
    #         else:
    #             layer.extend([cur_node.left, cur_node.right])
    #             out.extend([l, r])
    #             if l != 'null' or r != 'null':
    #                 layer_flg = 1
    #             if len(queue)==0:
    #                 queue.extend(layer)
    #                 layer = []
    #                 layer_flg = 0
    #
    #     return ','.join(out)
    #
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if data == '':
    #         return None
    #     data_list = data.split(',')
    #     root = TreeNode(data_list.pop(0))
    #     parents = [root]
    #     layer = []
    #     while len(data_list)>0:
    #         while len(parents)>0:
    #             node = parents.pop(0)
    #             if len(data_list) == 0:
    #                 break
    #             if data_list[0] != 'null':
    #                 node.left = TreeNode(data_list.pop(0))
    #                 layer.append(node.left)
    #             else:
    #                 data_list.pop(0)
    #             if len(data_list) == 0:
    #                 break
    #             if data_list[0] != 'null':
    #                 node.right = TreeNode(data_list.pop(0))
    #                 layer.append(node.right)
    #             else:
    #                 data_list.pop(0)
    #         parents = layer
    #         layer = []
    #
    #     return root
    def serialize(self,root):
        results = []
        cur_layer_nodes = [root]
        if root is None:
            return ''
        while(True):
            flg = 0
            next_layer_nodes = []
            for node in cur_layer_nodes:
                if node is None:
                    results.append('null')
                else:
                    results.append(node.val)
                    if node.left is not None:
                        next_layer_nodes.append(node.left)
                        flg = 1
                    else:
                        next_layer_nodes.append(None)
                    if node.right is not None:
                        next_layer_nodes.append(node.right)
                        flg = 1
                    else:
                        next_layer_nodes.append(None)
            cur_layer_nodes = next_layer_nodes
            if not flg:
                break
        return ','.join(results)


    def deserialize(self,data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data_list = data.split(',')
        root = TreeNode(data_list.pop(0))
        parents = [root]
        layer = []
        while len(data_list)>0:
            while len(parents)>0:
                node = parents.pop(0)
                if len(data_list) == 0:
                    break
                if data_list[0] != 'null':
                    node.left = TreeNode(data_list.pop(0))
                    layer.append(node.left)
                else:
                    data_list.pop(0)
                if len(data_list) == 0:
                    break
                if data_list[0] != 'null':
                    node.right = TreeNode(data_list.pop(0))
                    layer.append(node.right)
                else:
                    data_list.pop(0)
            parents = layer
            layer = []

        return root

if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    ans = ser.serialize(deser.deserialize(''))
    print(ans)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
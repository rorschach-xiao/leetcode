class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        cur_layer_list = [root]
        if root is None:
            return '[]'
        while (True):
            next_layer_list = []
            last_layer = True
            cur_layer_result = []
            for node in cur_layer_list:
                if node is not None:
                    cur_layer_result.append(str(node.val))
                    if node.left is not None:
                        next_layer_list.append(node.left)
                    else:
                        next_layer_list.append(None)
                    if node.right is not None:
                        next_layer_list.append(node.right)
                    else:
                        next_layer_list.append(None)
                    last_layer = False
                else:
                    cur_layer_result.append('null')
            if last_layer:
                break
            result.extend(cur_layer_result)
            cur_layer_list = next_layer_list

        return '['+','.join(result)+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        result = list(data.replace(' ','').split('[')[1].split(']')[0].split(','))
        root_val = result.pop(0)
        if root_val == '' or root_val == 'null':
            return None
        else:
            root_node = TreeNode(int(root_val))
        cur_layer = 0
        last_layer_nodes = [root_node]
        while(len(result)>0):
            cur_layer_nodes = []
            cur_layer += 1
            for i in range(2 * len(last_layer_nodes)):
                if len(result) == 0 :
                    break
                if i % 2 == 0:
                    last_root = last_layer_nodes.pop(0)
                if last_root is not None:
                    cur_layer_val = result.pop(0)
                    if cur_layer_val != 'null' :
                        new_node = TreeNode(int(cur_layer_val))
                        if i % 2 == 0:
                            last_root.left = new_node
                        else:
                            last_root.right = new_node
                        cur_layer_nodes.append(new_node)
                    else:
                        cur_layer_nodes.append(None)

            last_layer_nodes = cur_layer_nodes
        return root_node

if __name__ == '__main__':
    codec = Codec()
    data = '[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]'
    root = codec.deserialize(data)
    ser_tree = codec.serialize(root)
    print(ser_tree)









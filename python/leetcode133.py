from typing import Optional
from utils.Graph import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        top_node = Node(node.val)
        queue = [node]
        node_set = {node.val: top_node}
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.val not in node_set:
                new_node = Node(cur.val)
                node_set[cur.val] = new_node
            else:
                new_node = node_set[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in node_set:
                    next_node = Node(neighbor.val)
                    node_set[neighbor.val] = next_node
                    queue.append(neighbor)

                new_node.neighbors.append(node_set[neighbor.val])

        return node_set[node.val]

if __name__ == '__main__':
    solution = Solution()
    G = Node.adjList_2_graph([[2,4],[1,3],[2,4],[1,3]])
    G_copy = solution.cloneGraph(G)
    print(Node.graph_2_adjList(G_copy))

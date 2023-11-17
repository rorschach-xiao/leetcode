class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @classmethod
    def adjList_2_graph(cls, adjList):
        n = len(adjList)
        if n == 0:
            return None
        node_list = []

        for i in range(1, n + 1):
            node_list.append(cls(i))
        for i in range(n):
            cur = node_list[i]
            neighbor = adjList[i]
            cur.neighbors = [node_list[p - 1] for p in neighbor]
        return node_list[0]

    @classmethod
    def graph_2_adjList(cls, node):
        val2adj = {}
        node_set = {}
        queue = [node]
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.val not in node_set:
                node_set[cur.val] = cur

            cur_neighbors = []
            for neighbor in cur.neighbors:
                cur_neighbors.append(neighbor.val)
                if neighbor.val not in node_set:
                    queue.append(neighbor)
            val2adj[cur.val] = cur_neighbors
        n = len(val2adj)
        adjList = []
        for i in range(1, n+1):
            adjList.append(val2adj[i])
        return adjList


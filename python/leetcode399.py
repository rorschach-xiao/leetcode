from typing import List


class Solution:
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     node_map = {}
    #     cnt = 0
    #     equations_idx = []
    #     for equation in equations:
    #         x1, x2 = equation
    #         if x1 in node_map:
    #             node1 = node_map[x1]
    #         else:
    #             node_map[x1] = cnt
    #             node1 = cnt
    #             cnt += 1
    #         if x2 in node_map:
    #             node2 = node_map[x2]
    #         else:
    #             node_map[x2] = cnt
    #             node2 = cnt
    #             cnt += 1
    #         equations_idx.append([node1, node2])
    #     # initialize the unionfind set
    #     unionFind = UnionFind(cnt)
    #     for i, eq in enumerate(equations_idx):
    #         unionFind.union(eq[0], eq[1], values[i])
    #     res = []
    #     for q in queries:
    #         if q[0] not in node_map or q[1] not in node_map:
    #             res.append(round(-1.0, 5))
    #         else:
    #             x = node_map[q[0]]
    #             y = node_map[q[1]]
    #             root_x = unionFind.find(x)
    #             root_y = unionFind.find(y)
    #             if root_x != root_y:
    #                 res.append(round(-1.0, 5))
    #             else:
    #                 res.append(round(unionFind.weight[x] / unionFind.weight[y], 5))
    #
    #     return res
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        node = {}
        for eq in equations:
            if eq[0] not in node:
                node[eq[0]] = len(node)
            if eq[1] not in node:
                node[eq[1]] = len(node)
        unionFind = UnionFind(len(node))
        for eq, val in zip(equations, values):
            unionFind.union(node[eq[1]], node[eq[0]], val)

        for query in queries:
            if query[0] not in node or query[1] not in node:
                res.append(round(-1, 5))
            else:
                ind1 = node[query[0]]
                ind2 = node[query[1]]
                parent1 = unionFind.find(ind1)
                parent2 = unionFind.find(ind2)
                if parent1 != parent2:
                    res.append(round(-1, 5))
                else:
                    res.append(round(unionFind.weight[ind2] / unionFind.weight[ind1], 5))
        return res

class UnionFind():
    def __init__(self, n):
        self.weight = [1.0 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def union(self, x, y, v):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = v * self.weight[y] / self.weight[x]

    def find(self, x):
        if x != self.parent[x]:
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[origin]
        return self.parent[x]

if __name__ == '__main__':
    solution = Solution()
    equations = [["a","b"],["e","f"],["b","e"]]
    values = [3.4,1.4,2.3]
    queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
    print(solution.calcEquation(equations,values,queries))


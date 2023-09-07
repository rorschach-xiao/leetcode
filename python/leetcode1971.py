class Solution:
    # 并查集
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        p = [i for i in range(n)]
        def find(x):
            if p[x] != x:
                # 路径压缩
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            p[pa] = pb

        for edge in edges:
            union(edge[0],edge[1])
        ps = find(source)
        pd = find(destination)
        return ps == pd

    # dfs
    # def validPath(self, n: int, edges, source: int, destination: int) -> bool:
    #     self._graph = {}
    #     self.vis = set()
    #     for edge in edges:
    #         v1, v2 = edge[0], edge[1]
    #         if v1 not in self._graph:
    #             self._graph[v1] = [v2]
    #         else:
    #             self._graph[v1].append(v2)
    #         if v2 not in self._graph:
    #             self._graph[v2] = [v1]
    #         else:
    #             self._graph[v2].append(v1)
    #
    #     return self.dfs(source, destination)
    #
    # def dfs(self, src, dst):
    #     if src == dst:
    #         return True
    #     self.vis.add(src)
    #     for v in self._graph[src]:
    #         if v not in self.vis and self.dfs(v,dst):
    #             return True
    #     return False

if __name__ == '__main__':
    solution = Solution()
    n = 6
    edges = [[0,1],[0,2], [3,5],[5,4],[4,3]]
    src = 0
    dst = 5
    print(solution.validPath(n, edges, src, dst))

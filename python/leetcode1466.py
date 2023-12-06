from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {}
        # convert paths to adjecent map
        for path in connections:
            if path[0] not in adj:
                adj[path[0]] = [(path[1], 1)]
            else:
                adj[path[0]].append((path[1], 1))
            if path[1] not in adj:
                adj[path[1]] = [(path[0], 0)]
            else:
                adj[path[1]].append((path[0], 0))

        visit = set([0])
        ans = 0

        def dfs(city):
            nonlocal ans
            for neighbor, direction in adj[city]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)
                    if direction == 1:
                        ans += 1

        dfs(0)
        return ans
from collections import deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0
        graph = {}
        # construct an indirection graph
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in graph:
                    graph[stop] = set([i])
                else:
                    graph[stop].add(i)
        routes = [set(stops) for stops in routes]

        # BFS
        visited = set()
        visitedRoute = set()
        queue = deque([(source, 0)])
        visited.add(source)
        while queue:
            curStop, curNumBuses = queue.popleft()
            if curStop == target:
                return curNumBuses
            if curStop not in graph:
                break
            for nextRoute in graph[curStop]:
                if nextRoute not in visitedRoute:
                    visitedRoute.add(nextRoute)
                    for stop in routes[nextRoute]:
                        if stop not in visited:
                            visited.add(stop)
                            queue.append((stop, curNumBuses + 1))
        return -1

if __name__ == '__main__':
    solution = Solution()
    routes = [[1,2,7],[3,6,7]]
    source = 7
    target = 6
    print(solution.numBusesToDestination(routes, source, target))
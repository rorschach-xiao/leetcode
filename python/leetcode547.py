from collections import deque
from typing import List


class Solution:

    # BFS
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     n = len(isConnected)
    #     ans = 0
    #     visit = set()
    #     for i in range(n):
    #         if i not in visit:
    #             ans += 1
    #             queue = deque()
    #             queue.append(i)
    #             while queue:
    #                 cur_city = queue.popleft()
    #                 visit.add(cur_city)
    #                 for j in range(n):
    #                     if isConnected[cur_city][j] == 1 and j not in visit:
    #                         queue.append(j)
    #     return ans

    # find union

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(val):
            if parents[val] != val:
                parents[val] = find(parents[val])
            return val

        def union(a, b):
            parents[find(a)] = find(b)

        n = len(isConnected)
        parents = [i for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return sum([parents[i] == i for i in range(n)])

if __name__ == '__main__':
    solution = Solution()
    solution.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])




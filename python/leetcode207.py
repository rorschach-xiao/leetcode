from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preNum = [0 for _ in range(numCourses)]
        edges = {}
        queue = []
        m = numCourses
        for pre in prerequisites:
            preNum[pre[0]] += 1
            if pre[1] not in edges:
                edges[pre[1]] = [pre[0]]
            else:
                edges[pre[1]].append(pre[0])
        for i, n in enumerate(preNum):
            if n == 0:
                queue.append(i)
        while len(queue) != 0:
            cur = queue.pop(0)
            m -= 1
            if cur in edges:
                for neigh in edges[cur]:
                    preNum[neigh] -= 1
                    if preNum[neigh] == 0:
                        queue.append(neigh)
        return m == 0
if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1,0], [0, 1]]))